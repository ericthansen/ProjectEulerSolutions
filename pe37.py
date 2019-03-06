# Truncatable primes
# Problem 37 
# The number 3797 has an interesting property. 
#Being prime itself, it is possible to continuously remove digits 
#from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
#Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable 
#from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

##Use prime sieve, then pass thru again with additional check of truncatability
##upon second look, can probably quickly generate candidates by appending 2,3,5,7 to the prior list of truncatables...or along those lines.  fortunately, this works
cap=10**6
import math
import time as t

def isTP(n,primes):
    #istp=True
    currn=str(n)
    #print('currn',currn)
    for i in range(len(str(n))-1):
        currn=currn[1:]
        #print('currn',currn)
        if(int(currn) not in primes):
            return False
    currn=str(n)
    #print('currn',currn)
    for i in range(len(str(n))-1):
        currn=currn[0:len(currn)-1]
        #print('currn',currn)
        if(int(currn) not in primes):
            return False  
    print(n,'is truncatable')      
    return True

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
print('sievedone with',len(primes),'primes')
print('testing 3797',isTP(3797,primes))
#print('testing 5',isTP(5,primes))
s=0
count=0
index=0
sThru7=2+3+5+7
for p in primes:
    index+=1
    #if(index%1000==0):print("on the",index,"th prime,",p)
    if(isTP(p,primes)):
        s+=p
        count+=1
    if(count>=11+4):
        break
s=s-sThru7
print('the sum of the first',count-4,'truncatable primes is',s)