# Digit factorials
# Problem 34 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

##
import time as t

from math import factorial as f
print(f(1),f(2),f(3),f(4),f(5),f(6),f(7),f(8),f(9))
def check(x):
    s=str(x)
    left=0
    #print(f(1),f(2),f(3),f(4),f(5),f(6),f(7),f(8),f(9))
    d={'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}
    for i in range(len(s)):
        left+=d[s[i]]
        #left+=f(int(s[i]))
    if(left==x):
        return True
    else:
        return False
#print(check(145))
tt=t.time()
lt=t.time()
a=[]
for i in range(3,10**7):
    if(i%100000==0):
        #print(t.time()-tt,t.time()-lt,i)
        #lt=t.time()
        pass
    if(check(i)):
        #print(i)
        a.append(i)

print(a,sum(a))