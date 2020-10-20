"""Contains tests for schroedingersolver module"""

import schroedingersolver
import numpy as np
import os.path



result5.1 = (np.loadtxt("energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
result5.2 = (np.loadtxt("energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
result5.3 = (np.loadtxt("energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
result5.4 = (np.loadtxt("energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
result5.5 = (np.loadtxt("energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))

testdata5.1 = (np.loadtxt("test-data", "5.1", "energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
testdata5.2 = (np.loadtxt("test-data", "5.2", "energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
testdata5.3 = (np.loadtxt("test-data", "5.3", "energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
testdata5.4 = (np.loadtxt("test-data", "5.4", "energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))
testdata5.5 = (np.loadtxt("test-data", "5.5", "energies.dat", "expvalues.dat", "potential.dat", "wavefunctions.dat"))

results = [(result5.1, testdata5.1), (result5.2, testdata5.2), (result5.3, testdata5.3), (result5.4, testdata5.4), (result5.5, testdata5.5)]

@pytest.mark.parametrize("paar", results)
def test_results(paar):
    Ergebnis, Testwert = paar
    assert






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