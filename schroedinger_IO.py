#!/usr/bin/env python3
import numpy as np


def read_input(file_location):
    """reads input file and produces according variables

    Args:
        filename:
            name of inputfile in subdirectory 'input'

    Returns:
        newdata: an array containing the following variables as rows:
            -mass: mass of particle
            -xMin_xMax: touple of lower and upper boundaries
            -nPoint: number of X-values
            -interpolation: type of interpolation as number form 0 to 2
            -number of given Points for interpolation
            -points: matrix with set poits of curve
    """
    alldata = []
    with open(file_location) as fp:
        for line in fp:
            alldata.append(line.strip())
    dataline_y = 0
    for dataline in alldata:
        alldata[dataline_y] = dataline.split("#")[0].strip().split()
        dataline_y += 1

    if alldata[3] == ['linear']:
        alldata[3] = [0]
    elif alldata[3] == ['polynomial']:
        alldata[3] = [1]
    elif alldata[3] == ['cspline']:
        alldata[3] = [2]

    newdata = np.zeros((len(alldata), 3))
    line_y = 0
    for line in alldata:
        line_x = 0
        for coll in alldata[line_y]:
            newdata[line_y, line_x] = alldata[line_y][line_x]
            line_x += 1
        line_y += 1

    return newdata


def save_results(expvalues, energs, wavefuncts, potential):
    """writes results into .dat files

    Args:
        expvalues: array of expected location and deviation
        energs: 1D Array of calculated energies of the
            corresponding wavefunctions
        wavefuncts: Array of values for x-axis and amplitude
            of corresponding wavefunctions
        potential: Array of values for x-axis and corresponding potential
    """
    np.savetxt("expvalues.dat", expvalues)
    np.savetxt("energies.dat", energs)
    np.savetxt("wavefunctions.dat", wavefuncts)
    np.savetxt("potential.dat", potential)