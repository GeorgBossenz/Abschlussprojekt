#!/usr/bin/env python3
"""routines for visualizing results from schroedingersolver"""
import numpy as np
import matplotlib.pyplot as plt
import argparse

_DESCRIPTION = "visualizer for the obtained results from the schroedingersolver"

def main():
    """visualizer for the obtained results from the schroedingersolver

    Args:
        directory:
            directory of results from schroedingersolver
    """

    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    msg = 'Scale factor'
    
    args = parser.parse_args()

    def data_visualizer(args.directory, scale=1):
        """reads and plots data from input

        Args:
            scale: directory, scales the wavefunctions, default = no scaling
        """

        plt.subplot(1, 2, 1)

        potential = np.loadtxt(args.directory, "potential.dat")
        xx = potential[:, 0]
        y1 = potential[:, 1]

        aa = np.loadtxt(args.directory, "wavefunctions.dat")
        bb = np.loadtxt(args.directory, "energies.dat")
        cc = np.loadtxt(args.directory, "expvalues.dat")

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
                plt.plot(xx, aa[:, plotnr + 1] * scale + wert, color=color)
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
    main()
