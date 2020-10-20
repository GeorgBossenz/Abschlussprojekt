#!/usr/bin/env python3
"""routines for visualizing results from schroedingersolver"""
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os.path

_DESCRIPTION = "visualizer for the obtained results from the schroedingersolver"



def data_visualizer(directory='', scale=''):
    """reads and plots data from input

    Args:
    scale: directory, scales the wavefunctions, default = no scaling
    """

    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default=directory, help=msg)
    msg = 'Scale factor'
    parser.add_argument('scale', type=float, help=msg)
    args = parser.parse_args()

    plt.subplot(1, 2, 1)

    potential = (np.loadtxt(os.path.join(args.directory, "potential.dat")))
    xx = potential[:, 0]
    y1 = potential[:, 1]

    aa = (np.loadtxt(os.path.join(args.directory, "wavefunctions.dat")))
    bb = (np.loadtxt(os.path.join(args.directory, "energies.dat")))
    cc = (np.loadtxt(os.path.join(args.directory, "expvalues.dat")))

    plotnr = 0
    for wert in bb:
        eigenwert = []
        for xwert in potential:
            eigenwert.append(wert)
        plt.plot(xx, eigenwert, color="grey")

        if plotnr % 2:
            color = "red"
        else:
            color = "blue"
        plt.plot(xx, aa[:, plotnr + 1] * args.scale + wert, color=color)
        plt.plot(cc[plotnr, 0], wert, marker="x", color="green", mew=2)
        plotnr += 1
    plt.plot(xx, y1, color="black", scaley=False)

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
        plt.plot(cc[plotnr, 1], wert, marker="+", color="violet",
                 markersize=12, mew=2)
        plotnr += 1

    plt.xlabel("[Bohr]")
    plt.title("sigma x")
    plt.savefig('curves.pdf', format='pdf')


if __name__ == '__main__':
    data_visualizer()
