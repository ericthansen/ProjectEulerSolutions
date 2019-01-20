# Digit fifth powers
# Problem 30 
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

##Note that 9**5 = 59049, with 5 digits.  So we can limit our investigation to 
##numbers that have 6 or fewer digits
p=5
def digs(x):
    return list(str(x))
nums=[]
for n in range(2,10**(p+2)):
    # if(n%100000==0):
    #     print(n)
    l=digs(n)
    tot=0
    for d in l:
        dint=int(d)
        tot+=dint**p
    if(tot==n):
        nums.append(n)
print(nums)
print(sum(nums))