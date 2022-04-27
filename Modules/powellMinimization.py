# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:25:25 2022

xMin, nCyc = powell(F, x, h=0.1, tolerance=1.0e-6)
Powell's method of minimizing user-supplied function F(x)

x = starting point
h = initial search increment used in 'bracket'
xMin = minimum point
nCyc = number of cycles

Extracted from "Numerical Methods in Engineering with Python",
de Jaan  Kiusalaas (2005) Cambridge University Press

@author: Bruno M. Breggia
"""

import numpy as np
from Modules.goldSearch import bracket, goldSearch
from Modules.exceptions import DivergenceError

def powell(Func, x0, step=0.1, tolerance=1.0e-6):
    
    x = x0
    direction = np.zeros(shape=x0.shape)
    
    # dir_func = lambda s: Func(*(x+s*direction))
    def dir_func(s):
        nonlocal x, direction
        displacement = x + s*direction
        return Func(*displacement)
    
    n = len(x)
    df = np.zeros(shape=x.shape, dtype=np.float64)
    u = np.identity(n)
    for j in range(30):
        xOld = x[:]
        fOld = Func(*xOld)
        # first n lines searches record decreases of Func
        for i in range(n):
            direction = u[i]
            a, b = bracket(dir_func, 0.0, step)
            s, fMin = goldSearch(dir_func, a, b)
            df[i] = fOld - fMin
            fOld = fMin
            x = x + s*direction
        # last line search in the cycle
        direction = x - xOld
        a, b = bracket(dir_func, 0.0, step)
        s, fLast = goldSearch(dir_func, a, b)
        x += s*direction
        # check for convergence
        if np.sqrt( np.dot(x-xOld, x-xOld)/n ) < tolerance:
            return x, j+1
        # Identify biggest decrease and update search directions
        iMax = int(np.argmax(df))
        for i in range(iMax, n-1):
            u[i] = u[i+1]
            u[n-1] = direction
    
    raise DivergenceError("The Powell method could not converge")

