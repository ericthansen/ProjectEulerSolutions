# Consecutive prime sum

# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime 
#below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds 
#to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most 
#consecutive primes?


#note, the higher the prime, the longer potential chain.  Search just the last 1000 highest primes under 1 million.
from math import *
#from itertools import permutations
cap=10**6

def primeSieve(z):
    sieve=list(range(2,z+1))
    primes=[]
    primed={}
    for c in range(len(sieve)):
        if sieve[c]!=None:
            primes.append(sieve[c])
            primed[sieve[c]]=''
            currprime=sieve[c]
            currInd=c+currprime
            while currInd<len(sieve):
                sieve[currInd]=None
                currInd+=(currprime)
    return primes, primed
primes,primed=primeSieve(cap)
print('sievedone',max(primes),'sieve size:',len(primes))

maxlen=0
maxprime=0
for p in range(len(primes)-1,len(primes)-1000,-1):
    if(p%1000==0):
        print(p,primes[p],'maxlen',maxlen,'maxprime',maxprime)
    for i in range(p):
        shift=0
        currsum=0
        while(currsum<primes[p]):
            currsum+=primes[i+shift]
            shift+=1
        if currsum==primes[p]:
            if(shift>maxlen):
                maxlen=shift
                maxprime=primes[p]
print('maxprime:',maxprime,'maxlen',maxlen)