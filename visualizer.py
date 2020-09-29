"routines for visualizing results from schroedinger-solver"
import numpy as np
import matplotlib.pyplot as plt


def data_visualizer():
    "reads and plots data from input"

    %matplotlib inline
    potential = 1 #the right inputs, variable types n stuff missing
    xMin_xMax = -10, 10,
    nPoint = 100
    potential = np.matrix(1,2)

#ist erstmal nur zum ausprobieren, x-achse wird später durch
#die erste spalte vom potentail ersetzt

    xMin, xMax = xMin_xMax

    xx = np.linspace(xMin, xMax, nPoint, endpoint=True)
    y1 = (2,) * len(xx)

    plt.plot(xx, y1, color='green', linewidth=2.0, linestyle="-", label='2')

