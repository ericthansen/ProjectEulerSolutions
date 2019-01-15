# Lexicographic permutations
# Problem 24 
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math
p=10**6
l=['012','102','021','201']
print(sorted(l)[3])
print(math.factorial(10))
nPr=math.factorial(10)
#print(p/nPr)
f=0.27557319223985893
#mlp=2*10/10 + 7 * 9/10 + 
#maybe come back to this...

#perms=set()
perms=[]
digits=['0','1','2','3','4','5','6','7','8','9']
#print(digits)
for d1 in digits:
    ds1=digits.copy()
    ds1.remove(d1)
    for d2 in ds1:
        ds2=ds1.copy()
        ds2.remove(d2)
        for d3 in ds2:
            ds3=ds2.copy()
            ds3.remove(d3)
            for d4 in ds3:
                ds4=ds3.copy()
                ds4.remove(d4)
                for d5 in ds4 :
                    ds5 = ds4.copy()
                    ds5.remove(d5)
                    for d6 in ds5 :
                        ds6 = ds5.copy()
                        ds6.remove(d6)
                        for d7 in ds6:
                            ds7 = ds6.copy()
                            ds7.remove(d7)
                            for d8 in ds7:
                                ds8 = ds7.copy()
                                ds8.remove(d8)
                                for d9 in ds8:
                                    ds9 = ds8.copy()
                                    ds9.remove(d9)
                                    for d0 in ds9:
                                        ds0 = ds9.copy()
                                        ds0.remove(d0)
                                        p=d1+d2+d3+d4+d5+d6+d7+d8+d9+d0
                                        #perms.add(p)
                                        perms.append(p)
                                        #print(p)
                                        

print(len(perms))
perms=sorted(perms)
print(perms[10**6-1])