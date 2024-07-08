import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_func(x,y):
    return x+y, x*y

def test_func2(x,y):
    return x+y, x*y

test = test_func(1,2)
print(test)

print(test_func2(*test))