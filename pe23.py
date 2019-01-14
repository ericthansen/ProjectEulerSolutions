# Non-abundant sums
# Problem 23 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def d(n):
    #sum of proper divisors of n
    s=1
    i=2
    while i**2<=n:
        if(n%i==0):
            j=n/i
            s+=i
            if j!=i:
                s+=j
        i+=1
    return s

ulimit=28123
abundant=[]
for i in range(12,ulimit+1):
    if d(i)>i:
        abundant.append(i)
aset=set(abundant)
#print(aset)

def isAbSum(x):
    for i in aset:
        if i>x:
            return False
        if (x-i) in aset:
            return True
    return False

#candidates=list(range(1,ulimit+1))
#print(candidates)
NotAbSumTot=0
for c in range(1,ulimit+1):
    if not isAbSum(c):
        NotAbSumTot+=c

print(NotAbSumTot)

