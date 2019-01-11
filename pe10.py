# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math
z=2*10**6
sieve=list(range(2,z))
#print(sieve)
primes=[]
for c in range(len(sieve)):
    if sieve[c]!=None:
        primes.append(sieve[c])
        currprime=sieve[c]
        currInd=c+currprime
        while currInd<len(sieve):
            sieve[currInd]=None
            currInd+=(currprime)
print(sum(primes))