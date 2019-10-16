# #pe58.py

# Spiral primes
   
# Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


#Solution:
#this is straightforward/elegant if we compute an explicit formula for 
# entries along the diagonals. e.g. 4*x**2-11*x+8 for the bottom right diag.
#   For fun, let's also see if we can create the entire spiral
# exhaustively and check.  Finished that, but this winds up being much 
#more computationally expensive, so is omitted from this project code.

def isPrime(n) : 
  
    # Edge cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked to skip middle five numbers below 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def oddprimes2():
    layer=0 #consisting of only 1
    ratio=10#to get into the while loop
    p=0
    q=1
    while(ratio>0.1):
        layer+=1
        a=(2*layer+1)**2
        b=a-2*layer
        c=b-2*layer
        d=c-2*layer
        #print(a,b,c,d)
        #if(a in primed):
        #    p+=1
            #print(a,'prime!')
        if(isPrime(b)):
            p+=1
            #print(b,'prime!')
        if(isPrime(c)):
            p+=1
            #print(c,'prime!')
        if(isPrime(d)):
            p+=1
            #print(d,'prime!')
        q+=4
        ratio=p/q
        #print(p,q,ratio, layer)
    print("layer",layer,'sidelength:',2*layer+1)
    print('max prime',d)
    return 2*layer+1

def main3():
    print("starting main3")
    print('final answer:',oddprimes2())
main3()

