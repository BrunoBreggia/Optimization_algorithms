# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:07:55 2022

Use goldSearch to find x that minimizes 

    f(x) = 1.6x^3 + 3x^2 - 2x
    
subject to the constraint x >= 0.
Compare the result with the analytical solution.

@author: Bruno M. Breggia
"""

from Modules.goldSearch import bracket, goldSearch

# function to minimize
function = lambda x: 1.6*x**3 + 3*x**2 - 2*x

x0 = 1.0
step = 0.01
x1, x2 = bracket(function, x0, step)
x, fMin = goldSearch(function, x1, x2)
print(f"The minimum of f(x) is ({x}, {fMin})")

"""
The minimum of f(x) is
(0.2734941121981932, -0.28985978554959224)
"""


