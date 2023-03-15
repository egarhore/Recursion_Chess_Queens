import numpy as np
from QueenSolver import *

# Request for the proposed starting point
b_size = int(input('Enter a chess board size (even number): board is a square: default value set to 8: ') or 8)
x_start = int(input('Enter a starting row number from 1 to selected board size: default set to 1: ') or 1)
x_start -= 1

# Define the matrix
G = np.zeros((b_size, b_size))
H = np.empty([b_size, b_size], dtype=str)

# Run the Queen Solver
if queen_solver(x_start, 0, G, b_size):
    print('Done!!!\nSolution found\n')
    for x in range(b_size):
        for y in range(b_size):
            if G[x][y] == 1:
                H[x][y] = 'Q'
            else:
                H[x][y] = 'X'
    print('The Solution is shown below')
    print(H)
else:
    print('Recursion completed\nNo solution found\n')
