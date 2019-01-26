# Coin sums
# Problem 31 
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

##can iterate.  make dict of coin vals:
d={'c1':1,'c2':2,'c3':5,'c4':10,'c5':20,'c6':50,'c7':100,'c8':200}
tot=200

count=0
for i1 in range(int(tot/d['c8'])+1):
    left1=tot-i1*d['c8']
    for i2 in range(int(left1//d['c7'])+1):
        left2=left1-i2*d['c7']
        for i3 in range(int(left2//d['c6'])+1):
            left3=left2-i3*d['c6']
            for i4 in range(int(left3//d['c5'])+1):
                left4=left3-i4*d['c5'] 
                for i5 in range(int(left4//d['c4'])+1):
                    left5=left4-i5*d['c4'] 
                    for i6 in range(int(left5//d['c3'])+1):
                        left6=left5-i6*d['c3'] 
                        for i7 in range(int(left6//d['c2'])+1):
                            left7=left6-i7*d['c2'] 
                            for i8 in range(int(left7//d['c1'])+1):
                                left8=left7-i8*d['c1'] 
                                if(left8==0):
                                    count+=1
print(count)


