# Quadratic primes
# Problem 27 
# Euler discovered the remarkable quadratic formula:

# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n2+an+b, where |a|<1000 and |b|≤1000

# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

##This looks to be a doozy to brute force.  Let's see.  Turns out not so bad. 2 minutes, could be worse.
import math
def isprime(x):
    if(x<2):
        return False
    isprime=True
    for i in range(2,x):
        if(x%i==0):
            isprime=False
    return isprime
#print(isprime(41))
def ab(x):
    if(x<0):
        return -1*x
    else:
        return x
d={}
cap=1000
#checking one of the givens in the problem
# maxrun=0
# for b in range(1601,1602):
#     print('b',b)
#     for a in range(-79,-78):
#         maxp=0
#         for n in range(0,ab(b)):
#             if(isprime(n**2+a*n+b)):
#                 maxp=n
#             else:
#                 break
#         d[str(a)+'_'+str(b)]=maxp
#         maxrun=max(maxrun,maxp)
maxrun=0
for b in range(-cap,cap+1):
    print('b',b)
    for a in range(-cap+1,cap):
        maxp=0
        for n in range(0,ab(b)):
            if(isprime(n**2+a*n+b)):
                maxp=n
            else:
                break
        d[str(a)+'_'+str(b)]=maxp
        maxrun=max(maxrun,maxp)



#print(d)
#print(d['1_41'])
print(maxrun)
for k,v in d.items():
    if(v==maxrun):
        print(k,':',v,'product:',k*v )