# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math
z=600851475143
#print(math.factor(z))
a=13195
#z=a
#print(z/a)
# factors=[]
# for i in range(2,z):
#     if(z%i==0):
#         iprime=True
#         for j in range(2,math.ceil(i**.5)+1):
#             if(i%j==0):
#                 iprime=False
#         if iprime:
#             factors.append(i)
#         #i-=1
# print(factors)
print('test')
sieve=list(range(2,math.ceil(z**.5)))
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
print('halfway')
pf=[]
for p in primes:
    if z%p == 0:
        pf.append(p)
print(pf)
x=[71,839,1471,6857]
y=71*839*1471*6857
print(y)







