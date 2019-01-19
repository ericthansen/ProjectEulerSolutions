#pe26v2.py
# Reciprocal cycles
# Problem 26 
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#The modular reasoning and math was sufficiently complicated here that the coding is pretty inefficient.  Finished late at night so not bothering to go back and revise.
bound=1000
maxval=0
for d in range(1,bound):
    #remove all 2s and 10s
    #print(d)
    nex=d
    while(True):
        if(nex%2==0): 
            nex=nex/2
        else:
            break
    while(True):
        if(nex%5==0):
            nex=nex/5
        else:
            break
    nex2=nex

    k=1
    last=(10%nex2)% nex2
    while(True):
        if(nex2==1):
            break
        if(last==1):
            break
        else:
            k+=1
            last=last*(10%nex2) % nex2
    #print(d,k)
    #[maxval,val]=[max(maxval,k),d
    if(k>maxval):
        maxval=k
        val=d
        #print('updating maxval')

print(maxval,val)
