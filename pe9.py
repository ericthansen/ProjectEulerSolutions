# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for ib in range(2,999):
    leave=False
    for ia in range(1,332):
        c=(ia**2+ib**2)**.5
        if c==round(c) and ia+ib+c==1000:
            answer=[ia,ib,int(c)]
            leave=True
            break
    if leave:
        break
print(answer)
print(answer[0]*answer[1]*answer[2])