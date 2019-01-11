# Power digit sum
# Problem 16 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def sumdig(x):
    l=len(str(x))
    #print('l',l,' x',x)
    sumdig=0
    for i in range(1,l+1):
        currdig=x%10
        #print('currdig',currdig)
        x=x//10
        #print('l',l)
        sumdig+=currdig
    return sumdig

#print(sumdig(2**15))
print(sumdig(2**1000))

