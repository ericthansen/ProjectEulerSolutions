# #pe56.py
# Powerful digit sum
   
# Problem 56
# A googol ((10)^(100)) is a massive number: one followed by one-hundred 
#zeros; (100^100) is almost unimaginably large: one followed by two-hundred
# zeros. Despite their size, the sum of the digits in each number is 
#only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, 
#what is the maximum digital sum?
#
#strategy - could come up with max digits in such a number (e.g.)
#99^99, then multiply that # times 9...or brute force it
print(len(str(99**99)))
print(9*len(str(99**99)))
print("that's not it...so try...")
#this doesn't work, because 198 9's isn't of the form a**b.  So, let's
#look exhaustively.

def digsum(n):
    s=str(n)
    l=list(s)
    digs=0
    for i in l:
        digs+=int(i)
    return digs
#print(digsum(123))
maxdigsum=0
for a in range(1,100):
    for b in range(1,100):
        c=digsum(a**b)
        if(maxdigsum<c):
            maxdigsum=c
print(maxdigsum)
