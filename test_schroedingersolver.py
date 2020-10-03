"""Contains tests for schroedingersolver module"""

import schroedingersolver
import numpy as np
import os.path


def test_V1():
    datalocation = os.path.join("test-data", "5.1")
    schroedingersolver.main("5.1")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)


def test_V2():
    datalocation = os.path.join("test-data", "5.2")
    schroedingersolver.main("5.2")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)


def test_V3():
    datalocation = os.path.join("test-data", "5.3")
    schroedingersolver.main("5.3")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)


def test_V4():
    datalocation = os.path.join("test-data", "5.4")
    schroedingersolver.main("5.4")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)


def test_V5():
    datalocation = os.path.join("test-data", "5.5")
    schroedingersolver.main("5.5")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)


def test_V6():
    datalocation = os.path.join("test-data", "5.6")
    schroedingersolver.main("5.6")
    result = (np.loadtxt("potential.dat"),
              np.loadtxt("energies.dat"))
    testdata = (np.loadtxt(os.path.join(datalocation, "potential.dat")),
                np.loadtxt(os.path.join(datalocation, "energies.dat")))
    assert np.allclose(result, testdata)