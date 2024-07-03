from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
import numpy as np
import pandas as pd

test = np.array(np.arange(36).reshape(6, 6))

df = pd.DataFrame(data=test, columns=['a', 'b', 'c', 'd', 'e', 'f'])

d1_idx = np.array([0, 2, 5])
d2_idx = np.array([1, 3])

x = test[:,d1_idx]
y = test[:,d2_idx]

regressor = LinearRegression().fit(x.reshape(-1, 1), y.reshape(-1, 1))