# Highly divisible triangular number
# Problem 12 
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
import math

def numDiv(x):
    d=[]
    for i in range(1,math.ceil(x**.5)+1):
        if(x%i==0):
            d.append(i)
            d.append(x/i)
    #print('returning a numdiv',len(d))
    return len(d)
def go():
    curr=1
    tot=0
    maxdiv=0
    nd=0
    threshold=10**4
    freq=threshold/10**2
    while(True):
        tot+=curr
        curr+=1
        if(curr%(freq)==0):
            print('curr:',curr,', tot:',tot,"maxdiv:",maxdiv)
        if(curr>threshold):
            nd=numDiv(tot)
            maxdiv=max(nd,maxdiv)
            if(nd>500):
                break
    print(tot)

go()
