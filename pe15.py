# Lattice paths
# Problem 15 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# (see illustrations on website)

# How many such routes are there through a 20×20 grid?
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

print(nCr(40,20))