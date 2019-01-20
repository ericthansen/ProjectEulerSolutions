# Number spiral diagonals
# Problem 28 
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

## could do this with summation, or identify the regularity in increment...
s=1
inc=2
dr=3
dl=5
ul=7
ur=9
s=s+dr+dl+ul+ur
ring=5
while (ring<=1001):
    inc+=2
    dr=ur+inc
    dl=dr+inc
    ul=dl+inc
    ur=ul+inc
    s=s+dr+dl+ul+ur
    ring+=2
print(s)