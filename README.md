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

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/GoldenSectionSearch.png/1024px-GoldenSectionSearch.png" width="300" title="Golden Section Method">
</p>

Diagram of a golden-section search. The initial triplet of x values is {x1,x2,x3}. If f(x4)=f4a, 
the triplet {x1,x2,x4} is chosen for the next iteration. If f(x4)=f4b, the triplet {x2,x4,x3} 
is chosen.


### Powell's Method

Powell's method, strictly Powell's conjugate direction method, is an algorithm proposed by Michael 
Powell for finding a local minimum of a function. The function need not be differentiable, and no 
derivatives are taken.
The method minimises the function by a bi-directional search along each search vector, in turn. 
The bi-directional line search along each search vector can be done by Golden-section search or 
Brent's method.


<p align="center">
  <img src="https://api.europeana.eu/thumbnail/v2/url.json?size=w400&type=TEXT&uri=http%3A%2F%2Fwww.dmg-lib.org%2Fdmglib%2Fhandler%3Ffile%3Dimages_001%2Fdmg00020968023_%2F_tn_311x350_dmg00020968023_.png.jpg" width="300" title="Golden Section Method">
</p>
