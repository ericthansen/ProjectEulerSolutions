# Champernowne's constant

# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
champ="0."
i=1
while len(champ)<10**6+3:
    champ=champ+str(i)
    i+=1
#print(champ)
d1=int(champ[10**0+1])
d2=int(champ[10**1+1])
d3=int(champ[10**2+1])
d4=int(champ[10**3+1])
d5=int(champ[10**4+1])
d6=int(champ[10**5+1])
d7=int(champ[10**6+1])
print("answer:", d1*d2*d3*d4*d5*d6*d7)
