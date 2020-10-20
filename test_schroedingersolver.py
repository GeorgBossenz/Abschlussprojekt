"""Contains tests for schroedingersolver module"""
import pytest
import schroedingersolver
import numpy as np
import os.path

saved_results = ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6"]


@pytest.mark.parametrize("ntest", saved_results)
def test_examples(ntest):
    datalocation = os.path.join("test-data", ntest)
    schroedingersolver.main("input/" + ntest)

    potential = np.loadtxt("potential.dat")
    energies = np.loadtxt("energies.dat")
    expvalues = np.loadtxt("expvalues.dat")
    wavefunctions = np.loadtxt("wavefunctions.dat")

    potential_result = np.loadtxt(os.path.join(datalocation, "potential.dat"))
    energies_result = np.loadtxt(os.path.join(datalocation, "energies.dat"))
    expvalues_result = np.loadtxt(os.path.join(datalocation, "expvalues.dat"))
    wavefunctions_result = np.loadtxt(os.path.join(datalocation,
                                                   "wavefunctions.dat"))
    pot = np.allclose(potential, potential_result)
    energ = np.allclose(energies, energies_result)
    vals = np.allclose(expvalues, expvalues_result)
    waves = np.allclose(wavefunctions, wavefunctions_result)
    assert pot and energ and vals and waves
