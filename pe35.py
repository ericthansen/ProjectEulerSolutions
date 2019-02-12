# Circular primes
# Problem 35 
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

##Use prime sieve, then pass thru again with additional check of circularity
cap=10**6
import math
import time as t

def primeSieve(z):
    sieve=list(range(2,z+1))
    primes=[]
    for c in range(len(sieve)):
        if sieve[c]!=None:
            primes.append(sieve[c])
            currprime=sieve[c]
            currInd=c+currprime
            while currInd<len(sieve):
                sieve[currInd]=None
                currInd+=(currprime)
    return primes

primes=primeSieve(cap)
#print(primes)
print('sievedone')
#print(primes)
print('lenprimes is',len(primes))
def isCirc(x):
    s=str(x)
    curr=''
    isC=True
    #print('s is',s)
    for i in range(len(s)+1):
        curr=s[i:]+s[0:i]
        #print(' ',curr,i)
        if int(curr) in primes:
            pass
        else:
            return False
    return True

#print(isCirc(1234567))
#print(isCirc(197))
#print(isCirc(17))

def main():
    count=0
    #print('lenprimes is ',len(primes))
    tt=t.time()
    lt=t.time()
    for i in range(len(primes)):
        if i%(1000)==0:
            #print(t.time()-tt,t.time()-lt,i)
            #lt=t.time()
            #print('*********primeIndex:',i)
        if(isCirc(primes[i])):
            #print('***',primes[i])
            count+=1
    print('answer:',count)
main()
