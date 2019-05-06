# Sub-string divisibility

# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

#EH note, this literally means divisible by 2,3,5,7,... not just "non-prime"
from copy import *
def isSubStrDiv(n):
    s=str(n)
    divs=[2,3,5,7,11,13,17]
    for i in range(7):
        sub=s[i+1]+s[i+2]+s[i+3]
        t=int(sub)
        if (t%divs[i]!=0):
            return False
    return True
print('True testcase:',isSubStrDiv(1406357289))

def makePans(numdigs=10):
    if(numdigs!=10):
        print("Warning, this is made to work with 10 digits, you should customize it to use a different number")
    l=[]
    x=['1','2','3','4','5','6','7','8','9','0']
    firsts=['1','2','3','4','5','6','7','8','9']
    for d1 in firsts:
        #print('firstdig:',d1)
        s=''+d1
        x2=deepcopy(x)
        x2.remove(d1)
        for d2 in x2:
            s2=s+d2
            x3=deepcopy(x2)
            x3.remove(d2)
            for d3 in x3:
                s3=s2+d3
                x4=deepcopy(x3)
                x4.remove(d3)
                for d4 in x4:
                    s4=s3+d4
                    x5=deepcopy(x4)
                    x5.remove(d4)
                    for d5 in x5:
                        s5=s4+d5
                        x6=deepcopy(x5)
                        x6.remove(d5)
                        for d6 in x6:
                            s6=s5+d6
                            x7=deepcopy(x6)
                            x7.remove(d6)
                            for d7 in x7:
                                s7=s6+d7
                                x8=deepcopy(x7)
                                x8.remove(d7)
                                for d8 in x8:
                                    s8=s7+d8
                                    x9=deepcopy(x8)
                                    x9.remove(d8)
                                    for d9 in x9:
                                        s9=s8+d9
                                        x10=deepcopy(x9)
                                        x10.remove(d9)
                                        for d10 in x10:
                                            s10=s9+d10
                                            l.append(int(s10))
    return l
#Main:
pans=makePans()
#print('pans made')
s=0
for p in pans:
    if isSubStrDiv(p):
        s+=p
print('answer:',s)