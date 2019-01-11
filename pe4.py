# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import math
cap=999*999
#print(cap)
#print(len(str(int(546))))
cap=997799
leave=False
for i in range(cap,1,-1):
    if(i%1000==0):
        print('i is',i)
    if(str(i)!=str(i)[::-1]):
        continue
    print('i is',i)    
    for j in range(100,1000):
        if (i%j==0 and len(str(int(i/j)))==3):
            print("i is",i,'j is',j,'k is',i/j)
            leave=True
            break
    if leave:
        break
print("done")
