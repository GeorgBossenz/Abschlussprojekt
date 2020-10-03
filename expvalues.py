import numpy as np







potential_x = potential[:, 0]
wavesquared = wavefuncts * wavefuncts * potential_x[:, np.newaxis]
expected_x = np.sum(wavesquared, axis=0) * delta
mean_x = np.sum(wavesquared * potential_x[:, np.newaxis]) * delta
uncertainty = (mean_x - (expected_x **2)) ** 0.5
sigma = potential[:, 0]


