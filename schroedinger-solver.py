"routines for solving a time independant 1D-Sroedinger-equation"
import numpy as np

def read_input():
    """reads input file and produces according variables

    Returns:
        mass: mass of particle
        xMin_xMax: touple of lower and upper boundaries
        nPoint: number of X-values
        interpolation: type of interpolation
        points: matrix with set poits of curve
    """
    return mass, XMin_xMax, nPoint, interpolation, points


def potential_generator(xMin_xMax, nPoint, interpolation, points):
    """generates points of potential curve

    Args:
        xMin_xMax: touple of lower and upper boundaries
        nPoint: number of X-values
        interpolation: type of interpolation
        points: matrix with set points of curve

    Returns:
        potential: Matrix with corresponding x and V(x) values
        of potential curve
        delta: difference between neighboring x-values
    """
    #wie komme ich jetzt auf die y-werte??

    #so bekomme ich die Anzahl an inputs:
    for number_of_inputs in range(0,len(points)):
        for nn in range(0, nPoint):
            if points[0,number_of_inputs] >= XX[nn]:
                #hier muss ich mir noch überlegen wie ich YY auswähle und
                #ob das so geschickt ist




    potential = np.zeros((2,nPoint))
    XX = np.linspace(xMin, xMax, nPoint, endpoint=True)
    YY = []
    delta = abs(XX[1]-XX[0])
    #test values for y in matrix
    for nn in range(0, nPoint):
        YY.append(nn)
        #statt append hier lieber die variable an stelle nn durch den
        #jeweiligen y-wert ersetzen
    for index in range(0, nPoint):
        potential[0,index] = XX[index]
        potential[1,index] = YY[index]

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
#output should be file not variable
