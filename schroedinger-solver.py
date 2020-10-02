"routines for solving a time independant 1D-Sroedinger-equation"
import numpy as np
import scipy.interpolate as inter


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
# removes annotation of input data and splits lines into lists of
# individual inputs
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

    newdata = np.zeros((len(alldata), 3))
    line_y = 0
    for line in alldata:
        line_x = 0
        for coll in alldata[line_y]:
            newdata[line_y, line_x] = alldata[line_y][line_x]
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
    yy, xx = newdata.shape
    base = newdata[5:yy+1, 0:2]
    x_data = []
    y_data = []

    pointcount = 0
    for item in base[0]:
        x_data.append(base[pointcount, 0])
        y_data.append(base[pointcount, 1])
        pointcount += 1

# check if that works with floats
    if newdata[3, 0]:
        if newdata[3, 0] == 1:
            Vx = np.polyfit(x_data, y_data, yy - 6)
        else:
            Vx = inter.CubicSpline(x_data, y_data)
    else:
        Vx = inter.interp1d(x_data, y_data, kind='linear')

    potential = np.zeros((int(newdata[1, 2]), 2))
    XX_values = np.linspace(int(newdata[1, 0]), int(newdata[1, 1]),
                            int(newdata[1, 2]), endpoint=True)
    delta = XX_values[0] - XX_values[1]

    pointcount = 0
    for item in XX_values:
        potential[pointcount, 0] = item
        potential[pointcount, 1] = Vx(item)
        pointcount += 1

    mass = newdata[0, 0]
    return potential, delta, mass


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
    V_diskr = []
    for pair in potential:
        V_diskr.append(pair[1])

    content = []
    aa = 1 / (mass * (delta**2))

    content.append(aa * V_diskr[0])
    for columns in range(0, len(V_diskr)-1):
        content.append(-0.5 * aa)
        for num in range(0, len(V_diskr)-2):
            content.append(0)
        content.append(-0.5 * aa)
        content.append(aa * V_diskr[columns+1])
    hamiltonian = np.array(content)
    hamiltonian.shape = (len(V_diskr), len(V_diskr))

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
