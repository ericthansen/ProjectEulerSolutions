# Prime permutations

# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
#increases by 3330, is unusual in two ways: (i) each of the three terms 
#are prime, and, (ii) each of the 4-digit numbers are permutations of 
#one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
#primes, exhibiting this property, but there is one other 4-digit 
#increasing sequence.

# What 12-digit number do you form by concatenating the three terms in 
#this sequence?
from math import *
from itertools import permutations
cap=10**5
diff=3330
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

perms = [''.join(p) for p in permutations('stack')]

for prime in primes:
    if(len(str(prime)))!=4:
        continue
    perms=[''.join(p) for p in permutations(str(prime))]
    count=0#count of prime permutations
    answerperms=[]
    for perm in perms:
        try:
            _=primed[int(perm)]
            answerperms.append(int(perm))
            #count+=1
        except:
            pass
    #if count >=5:
    if(len(list(set(answerperms)))>=3):
        #3 because the prime itself will show up once, then 2 others
        ans=((list(set(answerperms))))
        ans.sort()
        for a in ans:
            if(a+diff in ans and a+2*diff in ans):
                print("Answer candidate:",ans)
print("Upon inspection, the 1487 group is given and the 379 group isn't all 4-digit")
print('Therefore, the answer is the 2699 group, in which the desired triple is:')
print('2969, 6299, 9629 --> 296962999629')
