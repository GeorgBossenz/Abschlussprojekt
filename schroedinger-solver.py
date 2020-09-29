"routines for solving a time independant 1D-Sroedinger-equation"
import numpy as np

def _read_input():
    """reads input file and produces according variables

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
    with open("input/5.1Potentialtopf") as fp:
        for line in fp:
            alldata.append(line.strip())
    dataline_y = 0
    for dataline in alldata:
        alldata[dataline_y] = dataline.split("#")[0].strip().split()
    #removes annotation of input data and splits lines into lists of individual inputs
        dataline_y += 1

    if alldata[3] == ['linear']:
        alldata[3] = [0]
    elif alldata[3] == ['polynomial']:
        alldata[3] = [1]
    elif alldata[3] == ['cspline']:
        alldata[3] = [2]
    #else:
        #alldata[3]
        #raise some kind of input error

    newdata = np.zeros((len(alldata),3))
    line_y = 0
    for line in alldata:
        line_x = 0
        for coll in alldata[line_y]:
            newdata[line_y,line_x] = alldata[line_y][line_x]
            line_x += 1
        line_y += 1

    return newdata


def _potential_generator(newdata):
    """generates points of potential curve

    Args:
        newdata: an array containing the user-input

    Returns:
        potential: Matrix with corresponding x and V(x) values
        of potential curve
        delta: difference between neighboring x-values
        mass: mass of particle, extracted from input-array
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


def _hamiltonmatrix_generator(potential, delta, mass):
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
