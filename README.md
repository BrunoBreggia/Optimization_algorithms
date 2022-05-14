# Optimization Algorithms

This project implements different numerical methods algorithms to optimize single and 
multiple-valued functions.

## Methods implemented
* [*Golden section search*](#Golden-Section-Search): one-dimentional optimization.
* [*Powell's method*](#Powell's-Method): optimization for multi-variable functions.

### Golden Section Search

The method operates by successively narrowing the range of values on the specified interval, 
which makes it relatively slow, but very robust. The technique derives its name from the fact 
that the algorithm maintains the function values for four points whose three interval widths 
are in the ratio φ:1:φ where φ is the golden ratio. These ratios are maintained for each 
iteration and are maximally efficient. Excepting boundary points, when searching for a minimum, 
the central point is always less than or equal to the outer points, assuring that a minimum is 
contained between the outer points.

### Powell's Method

Powell's method, strictly Powell's conjugate direction method, is an algorithm proposed by Michael 
Powell for finding a local minimum of a function. The function need not be differentiable, and no 
derivatives are taken.
The method minimises the function by a bi-directional search along each search vector, in turn. 
The bi-directional line search along each search vector can be done by Golden-section search or 
Brent's method.
$\{ x_0 \}$