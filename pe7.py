# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math
z=10**6
sieve=list(range(2,math.ceil(z)))
#print(sieve)
primes=[]
for c in range(len(sieve)):
    #if(c%1000==0):
    #    print ('c is',c)
    if sieve[c]!=None:
        primes.append(sieve[c])
        currprime=sieve[c]
        currInd=c+currprime
        while currInd<len(sieve):
            sieve[currInd]=None
            currInd+=(currprime)
print('halfway')
print('len of primes:',len(primes))
print(primes[10001-1])
