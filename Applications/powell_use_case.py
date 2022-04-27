# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:56:47 2022

@author: Bruno M. Breggia
"""

import numpy as np
from Modules.powellMinimization import powell

# function to minimize
def multivariateFunction(x, y):
    return 100*(y-x**2)**2 + (1-x)**2


x0 = np.array([-1, 1])  # starting point
xMin, cycles = powell(multivariateFunction, x0)
fMin = multivariateFunction(*xMin)
print(f"The minimum of my multivariate funciton is ({xMin}, {fMin})")
print(f"Done in {cycles} iterations")
