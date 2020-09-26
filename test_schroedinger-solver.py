"""Contains tests for schroedinger-solver module"""

import schroedinger-solver
import numpy as np

def test_potential_generator():
    result = schroedinger-solver.potential_generator((-2, 2), 5, linear, ((-1, 1), (1, 1)))
    assert result == np.array([-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1]), 1


def test_potential_generator():
    result = schroedinger-solver.potential_generator((-2, 2), 5, polinomial, ((-1, 1), (0, 0), (1, 1)))
    assert result == np.array([-2, 4], [-1, 1], [0, 0], [1, 1], [2, 4]), 1
    
    
def test_potential_generator():
    result = schroedinger-solver.potential_generator((-2, 2), 11, linear, ((-2, 0), (-0,5, 0), (-0,5, -10),(0,5, -10), (0,5, 0), (2, 0)))
    assert result == np.array([-2, 0], [-1,5, 0], [-1, 0], [0,5, 0], [0,5, -10], [0, -10], [0,5, -10], [0,5, 0], [1, 0], [1,5, 0], [2, 0]), 0,5
    