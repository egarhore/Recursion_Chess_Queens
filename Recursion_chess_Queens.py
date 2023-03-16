import datetime
import time

import numpy as np
from QueenSolver import *

# Start the timer
start_time = time.time()

# Request for the proposed starting point
d_properties = {}
with open('Input.txt') as f:
    for line in f:
        (key, val) = line.strip().split()
        d_properties[key] = val

# Get size of the structure
b_size = int(d_properties['Board_Size'])
x_start = int(d_properties['Start_point'])
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

# Complete process and show runtime
end_time = time.time()
run_time = end_time - start_time
run_time = str(datetime.timedelta(seconds=int(run_time)))
print('\n<<<<<<<<<<<<<>>>>>>>>>>>>>')
print('Process completed\n' + 'Total runtime = ' + run_time)
print('<<<<<<<<<<<<<>>>>>>>>>>>>>')
