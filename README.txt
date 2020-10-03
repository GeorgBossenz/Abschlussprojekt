**************************
Schödinger-equation solver
**************************

Programm for solvin time independent 1D schödinger-equations.

repository: https://github.com/GeorgBossenz/Abschlussprojekt



required modules:
	numpy
	scipy
	mathplotlib.pyplot
	pytest

To calculate relevant results from input, run schroedingersolver.py from the command line.

API documentation is located in /docs/_build/html/index.html.

The input should be named schrodinger.inp and be constructed according to the following  format:

schrodinger.inp:
2.0		# mass
-2.0 2.0 1999	# xMin xMax nPoint
1 5		# first and last eigenvalue to print
linear		# interpolation type
2		# nr. of interpolation points and xy declarations
-2.0  0.0
 2.0  0.0

The data schould be given in the follwing units:
distance: Bohr
energy: Hartree
mass: Electron-mass


The results are written into the follwing files, formatted as shown:
energies.dat:
E1
E2
...

potential.dat:
x1 		V(x1)
x2		V(x2)
...

wavefunctions.dat:
x1		Y1(x1)		Y2(x1)...
x2		Y1(x2)		Y2(x2)...
...

expvalues.dat
 <x1>	sigma(x1)
<x2>	sigma(x2)
...

