# Pandigital products
# Problem 32 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

##try exhaustive method.

pandigitals=[]
cap=98765

def isPandig(m1,m2,prod):
    alph=str(m1)+str(m2)+str(prod)
    l=[]
    if(len(alph)!=9):
        return False
    for i in range(len(alph)):
        if(alph[i]!='0'):
            #print('appending',alph[i])
            l.append(alph[i])
    alf=list(set(l))
    if(len(alf)==9):
        #print(alf)
        return True
    else:
        return False

#print(isPandig(123,456,789))
import math
import time as t
tt=t.time()
lt=t.time()
for prod in range(1,cap):
    if(prod%1000==0):
        #print('prod',prod)
        #print(t.time()-tt,'total sec')
        #print(t.time()-lt,'since last')
        lt=t.time()
    for m1 in range(1,int(math.ceil(prod**.5))):
        if(prod%m1==0):
            m2=prod//m1
            if(isPandig(m1,m2,prod)):
                pandigitals.append(prod)
panset=set(pandigitals)
sumPanDigs=sum(list(panset))
print(sumPanDigs)