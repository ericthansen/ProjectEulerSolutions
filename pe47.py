# Distinct primes factors

# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from math import *
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
print('Prime sieve created.')

def factors(y,primed):
    f=[]
    x=y
    primes=primed.keys()
    for p in primes:
        if x%p==0:
            while(x%p==0):
                f.append(p)
                x=int(x/p)
        if y==1:
            break
    try:
        f.remove(1)
    except:
        pass
    return sorted(f)

#print('test',factors(156,primed),list(set(factors(156,primed))))

def main():
    a=False
    b=False
    c=False
    d=False
    i=640
    consecutives=4
    while(not a or not b or not c or not d):
        if(i%10**3==0):
            print('on i:',i)
        f=factors(i,primed)
        setf=list(set(f))
        if(len(setf)==consecutives):
            if(a==False):
                a=True
            elif(b==False):
                b=True
            elif(c==False):
                c=True
            elif(d==False):
                d=True
        else:
            a=False
            b=False
            c=False
            d=False
        i+=1
    print('answer:',i-3-1)

main()
