#!/usr/bin/env python3
"""routines for solving a time independant 1D-Schroedinger-equation"""
import numpy as np
import scipy.interpolate as inter
import os.path
import numpy.linalg as linalg
import argparse
import schroedinger_IO as IO

_TOLERANCE = 0.000001
_DESCRIPTION = 'solver for schroedinger-equation'


def main(directory='.'):
    """solver for Schroedinger-equation

    Args:
        directory:
            directory of input file other than subdirectory 'input'
    """
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default=directory, help=msg)
    args = parser.parse_args()

    file_location = os.path.join(args.directory, "schrodinger.inp")
    newdata = IO.read_input(file_location)
    potential, delta, mass = potential_generator(newdata)
    hamiltonian = hamiltonmatrix_generator(potential, delta, mass)
    eigenvalues, eigenvectors = hamiltonmatrix_solver(hamiltonian)

    sortedvectors = eigenvectors[:, eigenvalues.argsort()]

    normfactors = []
    for ii in range(0, len(sortedvectors[0, :])):
        aa = sum(sortedvectors[:, ii] * sortedvectors[:, ii] * delta)
        aa = aa ** -0.5
        normfactors.append(aa)
    sortedvectors = sortedvectors * normfactors

    eigenvalues.sort()
    energs = np.transpose(eigenvalues[int(newdata[2, 0])-1:int(newdata[2, 1])])

    wanted_waves = sortedvectors[:, int(newdata[2, 0])-1:int(newdata[2, 1])]
    wavefuncs_x = potential[:, 0]
    wavefuncs_x.shape = (len(potential), 1)
    wavefuncts = np.concatenate((wavefuncs_x, wanted_waves), axis=1)

    expected_x, sigma = expvalues_calculator(wanted_waves, delta, potential)

    xyz, nvalues = np.shape(wanted_waves)
    expvalues = np.zeros((nvalues, 2))
    expvalues[:, 0] = expected_x
    expvalues[:, 1] = sigma
    IO.save_results(expvalues, energs, wavefuncts, potential)


def potential_generator(newdata):
    """generates points of potential curve

    Args:
        newdata: an array containing the user-input

    Returns:
        potential: Matrix with corresponding x and V(x) values
        of potential curve
        delta: difference between neighboring x-values
        mass: mass of particle, extracted from input-array
    """
    yy, xx = newdata.shape
    base = newdata[5:yy+1, 0:2]
    x_data = []
    y_data = []

    pointcount = 0
    for item in base:
        x_data.append(base[pointcount, 0])
        y_data.append(base[pointcount, 1])
        pointcount += 1

    V_x = False
    if newdata[3, 0]:
        if newdata[3, 0] == 1:
            coeffs = np.polyfit(x_data, y_data, yy - 6)
        else:
            V_x = inter.CubicSpline(x_data, y_data, bc_type='natural')
    else:
        V_x = inter.interp1d(x_data, y_data, kind='linear')

    npoints = int(newdata[1, 2])
    potential = np.zeros((int(newdata[1, 2]), 2))
    XX_values = np.linspace(int(newdata[1, 0]), int(newdata[1, 1]),
                            npoints, endpoint=True)
    delta = XX_values[1] - XX_values[0]

    if not V_x:
        YY_values = np.zeros(npoints)
        for pointcount in range(npoints):
            for power in range(yy - 5):
                YY_values[pointcount] += coeffs[power] * (XX_values[pointcount]
                    ** (yy - 6 - power))

        potential[:, 0] = XX_values
        potential[:, 1] = YY_values
    else:
        pointcount = 0
        for item in XX_values:
            potential[pointcount, 0] = item
            potential[pointcount, 1] = V_x(item)
            pointcount += 1

    mass = newdata[0, 0]
    return potential, delta, mass


def hamiltonmatrix_generator(potential, delta, mass):
    """generates the hamilton matrix

    Args:
        potential: Matrix with corresponding x and V(x) values
        of potential curve
        delta: difference between neighboring x-values
        mass: mass of particle

    Returns:
        hamiltonian: hamilton-matrix
    """
    ii, bb = potential.shape
    aa = 1 / (mass * (delta**2))

    hamiltonian = np.zeros((ii, ii))
    hamiltonian[0, 0] = potential[0, 1] + aa
    hamiltonian[0, 1] = -0.5 * aa
    hamiltonian[ii-1, ii-1] = potential[ii-1, 1] + aa
    hamiltonian[ii-1, ii-2] = -0.5 * aa

    for index in range(ii-2):
        hamiltonian[index+1, index] = -0.5 * aa
        hamiltonian[index+1, index+1] = potential[index+1, 1] + aa
        hamiltonian[index+1, index+2] = -0.5 * aa
    return hamiltonian


def hamiltonmatrix_solver(hamiltonian):
    """procedure to produce eigenvalues and corresponding eigenvectors
    of hamilton matrix

    Args:
        hamiltonian: hamilton matrix

    Returns:
        eigenvalues: list of aquired eigevalues
        eingenvectors: list of eigenvectors
    """

    eigenvalues, eigenvectors = linalg.eig(hamiltonian)

    return eigenvalues, eigenvectors


def expvalues_calculator(wanted_waves, delta, potential):
    """will calculate sigma and uncertainty

    Args:
        wanted_waves: array of discrete amplitudes of wavefunction
        delta:difference between neighboring x-values
        potential: Matrix with corresponding x and V(x) values
        of potential curve

    Returns:
        mean_x: 1D array of expected amplitudes
        sigma: 1D array of mean quadratic deviation from expected amplitude
    """
    potential_x = potential[:, 0]
    wavesquared = wanted_waves * wanted_waves * potential_x[:, np.newaxis]
    expected_x = np.sum(wavesquared, axis=0) * delta
    mean_x = np.sum(wavesquared * potential_x[:, np.newaxis], axis=0) * delta
    sigma = (mean_x - (expected_x ** 2)) ** 0.5
    return expected_x, sigma


if __name__ == '__main__':
    main()
