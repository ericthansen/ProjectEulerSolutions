# Pandigital multiples

# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

##example is 918273645
##so must be larger than that, but less than 10**10
##furthermore, it must start with 91 or higher, but 9 alone is already taken
##so consider 98, 97, ...91.
##will wind up exhaustive testing, but should be confident that answer is no more than 10^5
def isPan(n):
    s=str(n)
    x=[1,2,3,4,5,6,7,8,9]
    for i in range(len(s)):
        if int(s[i]) in x:
            x.remove(int(s[i]))
        else:
            return False
    return True
#print(isPan(192384576))
#print(isPan(918273645))
#print(isPan(918273644))
def makenum(n):
    tot=str(1*n)
    i=2
    while len(tot)<9:
        tot=tot+str(n*i)
        i+=1
    return int(tot)
#print(makepan(9))
  
maximum=0
for i in range(10**6):
    temp=makenum(i)
    if isPan(temp) and temp>maximum:
        maximum=temp
    if i% 10**5==0:
        print("at ",i," of 10**10")
        print('maximum is',maximum)
print('maximum:', maximum)
#     print(c)
