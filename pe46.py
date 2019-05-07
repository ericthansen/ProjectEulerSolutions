# Goldbach's other conjecture

# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

cap=10**6
import math
import time as t

def issumprimeandtwiceasquare(x, primed):
    for p in list(primed.keys()):
        if(p>=x):
            break
        remainder=x-p
        rem2=remainder/2
        rem2sqrt=rem2**.5
        if rem2sqrt==int(rem2sqrt):
            return p,rem2sqrt
    return None,None

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
print('sievedone')
print('test',issumprimeandtwiceasquare(15,primed))
print('test',issumprimeandtwiceasquare(27,primed))
for i in range(3,cap+1,2):
    try:
        _=primed[i]
    except:
        p,rem2sqrt=issumprimeandtwiceasquare(i,primed)
        if p==None:
            print('answer',i)
            break

