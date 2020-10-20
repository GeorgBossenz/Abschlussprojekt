"""Contains tests for schroedingersolver module"""

import schroedingersolver
import numpy as np
import os.path



@pytest.mark.parametrize()
def test_examples():
    datalocation = os.path.join("test-data", "5.1")
    schroedingersolver.main("input/5.1")

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
