# Reciprocal cycles
# Problem 26 
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def multOf2and5(n):
    r=False
    for k in range(1,cap):
            if (10**k % n == 0):
                if(r==False):
                    r=k
                else:
                    r=min(r, k)
            else:
                pass#return False
    return r


def part2f(d):
    r=False
    for k in range(1,cap):
        #may need to update this cap if we are topping out
        if (10**k % d == 1):
            if(r==False):
                r=k
            else:
                r=min(r,k)
    return r

def part3f(d):
    r=False
    for k2 in range(1,cap):
        for k3 in range(1,cap):
            if((10**(k2+k3) % d == 10**k3)):
                if(r==False):
                    r=k3
                else:
                    r=min(r,k3)
    return k3
cap=100
answer=0
ak0 = 0
ak1 = 0
ak3 = 0
for d in range(1,1000):
    #print(1/d)
    print(d)
    c=1/d
    #if c terminates, 10^k * 1/d = an integer; 10^k % d = 0; so d=2^a*5^b:
    k0=multOf2and5(d)
    
    if(k0):
        ak0=max(ak0,k0)
        #continue

    #if c is entirely repeating, then 10^k*c-c=c(10^k-1) is an integer; so d is a divisor of (10^k-1), or 10^k % d = 1 = 2^a*5^b % d:
    k1=part2f(d)
    
    if(k1):
        ak1=max(ak1,k1)
    #if c has a nonrepeating start, then repeats:
    #then there is a k2 such that 10^k2*c that has a totally repeating part
    #so then there is a k3 such that 10^k3*(10^k2*c-c)=10^(k3)*c*(10^k2-1)=c(10^(k2+k3)-10^k3) is an integer, so (10^(k2+k3) % d = 10^k3
    k3 = part3f(d)

    if(k3):
        ak3=max(ak3,k3)
    ansD=min(k0,k1,k3)
    print(k0,k1,k3)
    answer=max(answer,ansD)
print(answer,ak0,ak1,ak3)
