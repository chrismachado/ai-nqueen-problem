# IA N-Queens Problem
This code solve the most commum problem in Artificial Intelligence the N-Queen 
problem.

## N-Queen problem
The problem consist in to place N-queens on a chess NxN board, and them can't attack
each other.

![queenboard](images/board4.png)

## Hill Climbing Algorithm
Hill climbing attempts to maximize (or minimize) a target function f (x) 
where x is a vector of continuous and/or discrete values. At each iteration, 
hill climbing will adjust a single element in x and determine whether the change 
improves the value of f(x).

## Simulated Annealing
Simulated annealing (SA) is a probabilistic technique for approximating the global
 optimum of a given function. Specifically, it is a metaheuristic to approximate 
 global optimization in a large search space for an optimization problem. It is 
 often used when the search space is discrete (e.g., the traveling salesman 
 problem). 
 
 ## Getting Started
This code implements the aforementioned algorithms. To start, just run the main.py file.
After run that, answer the questions.
- Select the algorithm  you will use (1 - HC, 2 - SA).
- Define initial state (1 - Y, Any - N).
- Board size (4, 5, 8, etc).
- Iteration number.

If you chosen HC:
- HC common or HC random

If you chosen SA:
- Maximum number of disturbances
- Maximum number of success
- Initial temperature

The result will be on resource/newBoard.txt.