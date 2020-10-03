"routines for visualizing results from schroedinger-solver"
import numpy as np
import matplotlib.pyplot as plt


def data_visualizer():
    "reads and plots data from input"

    %matplotlib inline

    plt.subplot(1, 2, 1)

    potential = np.loadtxt("potential.dat")
    xx = potential[:, 0]
    y1 = potential[:, 1]

    aa = np.loadtxt("wavefunctions.dat")
    bb = np.loadtxt("energies.dat")
    cc = np.loadtxt("expvalues.dat")

    plotnr = 0
    for wert in bb:  #dort packen wir eine Liste mit den Eigenwerten hin
        eigenwert = []
        for xwert in potential:
            eigenwert.append(wert)
        plt.plot(xx, eigenwert, color="grey")

        if plotnr % 2:
            color = "red"
        else:
            color = "blue"
        plt.plot(xx, aa[:, plotnr + 1] + wert, color=color)
        plt.plot(cc[plotnr, 0], wert, marker="x", color="green", mew=2)
        plotnr += 1
    plt.plot(xx, y1, color="black", label="potential curve", scaley=False)


    plt.xlabel("x [Bohr]")
    plt.ylabel("Energy [Hartree]")
    plt.title("Potential, eigenstates, <x>")

    plt.subplot(1, 2, 2)

    plotnr = 0
    for wert in bb:
        eigenwert = []
        for xwert in potential:
            eigenwert.append(wert)
        plt.plot(xx, eigenwert, color="grey")
        plt.plot(cc[plotnr, 1], wert, marker="+", color="violet", markersize = 12, mew=2)
        plotnr += 1

    plt.xlabel("[Bohr]")
    plt.title("sigma x")
