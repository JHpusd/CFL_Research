import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

test = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])

print(np.max(test, axis=1))