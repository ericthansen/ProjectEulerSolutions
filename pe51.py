# Prime digit replacements

# Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out 
#that six of the nine possible values: 13, 23, 43, 53, 73, and 83, 
#are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, 
#this 5-digit number is the first example having seven primes among 
#the ten generated numbers, yielding the family: 56003, 56113, 56333, 
#56443, 56663, 56773, and 56993. Consequently 56003, being the first 
#member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not 
#necessarily adjacent digits) with the same digit, is part of an eight 
#prime value family.

from math import *
import time
#from itertools import permutations
cap=10**7
#starting=1270000
def primeSieve(z):
    sieve=list(range(2,z+1))
    primes=[]
    primed={}
    for c in range(len(sieve)):
        if sieve[c]!=None:
            primes.append(sieve[c])
            primed[sieve[c]]=c
            currprime=sieve[c]
            currInd=c+currprime
            while currInd<len(sieve):
                sieve[currInd]=None
                currInd+=(currprime)
    return primes, primed


a=time.time()
primes,primed=primeSieve(cap)
print('sievedone',max(primes),'sieve size:',len(primes))
b=time.time()
print('sieve time:',b-a)

def famSize(x, primes, primed):
    l=len(str(x))
    #print(l)
    m=[]
    famsizmax=0
    #ret=None
    #issue - need to enable #replacements from 1-l
    for i in range(l):
        #print(i)
        for j in range(i+1,l):
            #for jk in range(j+1,l):
              #for jkl in range(jk+1,l):
                famsiz=0
                if i==j :#:
                    continue
                else:
                    for k in range(10):
                        temp=str(x)
                        #temp[i]=str(k)
                        temp=temp[:i]+str(k)+temp[i+1:]
                        #temp[j]=str(k)
                        temp=temp[:j]+str(k)+temp[j+1:]
                        #temp=temp[:jk]+str(k)+temp[jk+1:]
                        #temp=temp[:jkl]+str(k)+temp[jkl+1:]
                        #print(temp)
                        temp=int(temp)
                        try:
                            _=primed[temp]
                            famsiz+=1
                            if(famsiz>famsizmax):
                                famsizmax=famsiz
                                #ret=
                        except:
                            pass
    return famsizmax

#print("testing 56003 (7): ",famSize(56003,primes,primed))    
#print("testing 13 (6): ",famSize(13,primes,primed))    
#216000
#primed[starting]
start=1#1664000#5761000
for i in range(start,len(primes),1):
    if(i%1000==0):
        print(i)
    x=famSize(primes[i],primes,primed)
    if x>=8:
        print('answer:',primes[i], 'famsize',x)
        break
print('finished')
c=time.time()
print('in total time',c-a,'; sievetime:',b-a,'famsizetime:',c-b)

