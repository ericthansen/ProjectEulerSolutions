#pe57.py

#For the sequence of fraction expansions for Sqrt(2), how many have a
#numerator with more digits than denominator?
#see visual at 
#https://projecteuler.net/problem=57

from fractions import Fraction as Fr
iterations=10**3

def addTwoUnderOne(x):
    return Fr(1,(x+2))
accum=0
answer=0
for _ in range(iterations):
    accum=addTwoUnderOne(accum)
    curranswer=1+accum
    #print(curranswer)
    n=curranswer.numerator
    d=curranswer.denominator
    if(len(str(n))>len(str(d))):
        answer+=1
        #print(n,d)
print(answer)