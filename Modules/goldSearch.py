# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:07:07 2022

a,b = bracket(f,xStart,h)
Finds the brackets (a,b) of a minimum point of the user-supplied 
scalar function f(x).
The search starts downhill from xStart with a step length h.

x,fMin = search(f,a,b,tol=1.0e-6)
Golden section method for determining x that minimizes the user
supplied scalar function f(x).
The minimum must be bracketed in (a,b).

Extracted from "Numerical Methods with Python"

@author: Bruno M. Breggia
"""

import math
from Modules.exceptions import MinimumNotFound

fi = (1+math.sqrt(5))/2
fi_prime =(-1+math.sqrt(5))/2

def bracket(func, x0, step):
    # evaluate at initial time
    y0 = func(x0)
    # evaluate at next timestep
    x1 = x0 + step
    y1 = func(x1)
    # determine downhill directions and change sign of h if needed
    if y1 > y0:
        step = -step
        x1 = x0 + step
        y1 = func(x1)
        # check if minimum between x2-step and x1+step
        if y1 > y0:
            return x1, x0-step
    # search loop
    for i in range(100):
        step *= fi
        x2 = x1 + step
        y2 = func(x2)
        if y2 > y1:
            return x0,x2
        x0, y0 = x1, y1
        x1, y1 = x2, y2
    raise MinimumNotFound("Bracket could not find a minimum")

def goldSearch(func, a, b, tolerance=1.0e-9):
    nIter = math.ceil(1/math.log(fi_prime) * math.log(tolerance/abs(b-a)))
    # First telescoping
    x1 = a*fi_prime + b*(1-fi_prime)
    f1 = func(x1)
    x2 = a*(1-fi_prime) + b*fi_prime
    f2 = func(x2)
    # Main loop
    for i in range(nIter):
        if f1 > f2:
            a = x1
            x1, f1 = x2, f2
            # calculate new step
            x2 = a*(1-fi_prime) + b*fi_prime
            f2 = func(x2)
        else:
            b = x2
            x2, f2 = x1, f1
            x1 = a*fi_prime + b*(1-fi_prime)
            f1 = func(x1)
    if f1 <= f2:
        return x1, f1
    return x2, f2














