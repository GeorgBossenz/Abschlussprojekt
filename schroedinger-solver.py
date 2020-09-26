"routines for solving a time independant 1D-Sroedinger-equation"
import numpy as np


def potential_generator(xMin_xMax, nPoint, interpolation, points):
    """generates points of potential curve

    Args:
        xMin_xMax: touple of lower and upper boundaries
        nPoint: number of X-values
        interpolation: type of interpolation
        points: matrix with set poits of curve

    Returns:
        potential: Matrix with corresponding x and V(x) values
        of potential curve
        delta: difference between neighboring x-values
    """
    return potential, delta


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
    return eigenvalues, eigenvectors

def expvalues_calculator(unknown):
    """will calculate sigma and uncertainty

    Args:

    Returns:

    """
    return sigma, uncertainty
