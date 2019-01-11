# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
####
#define constants to make customizeable
cap=10**3
n1=3
n2=5
#find number of times n1, n2 divide fully into cap minus 1
d1=(cap-1) // n1
d2=(cap-1) // n2
#use sum of first n integers formulas
s1 = (d1*(d1+1)/2)*n1
s2 = (d2*(d2+1)/2)*n2
###except this double counts numbers that are multiples of both 3 and 5!
###so we can subtract those out
d3=(cap-1) //(n1*n2)
s3=(d3*(d3+1)/2)*(n1*n2)
print(int(s1+s2-s3))

###alternately we can for-loop it, but this takes a lot longer!
s4=0
for i in range(1,cap):
    if(i%n1==0 or i%n2 ==0):
        s4+=i
print(int(s4))

