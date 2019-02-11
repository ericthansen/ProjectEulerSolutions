# Digit cancelling fractions
# Problem 33 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

## 2 * 2 digits can be done exhaustively

a=[]
import fractions as f
for den in range(10,100):
    for num in range(10,den):
        if(num==den):
            continue
        ns1=str(num)[0]
        ns2=str(num)[1]
        ds1=str(den)[0]
        ds2=str(den)[1]
        #print('firstcheck',ns1,ns2,ds1,ds2)
        if((ns2=='0' and ds2=='0')):
            continue
        if(ns1==ds1 and ds2!='0'):
            frac=f.Fraction(int(ns2),int(ds2))
        elif(ns1==ds2 and ds1!='0'):
            frac=f.Fraction(int(ns2),int(ds1))  
        elif(ns2==ds1 and ds2!='0'):
            frac=f.Fraction(int(ns1),int(ds2)) 
        elif(ns2==ds2 and ds1!='0'):
            frac=f.Fraction(int(ns1),int(ds1)) 
        else:
            frac=None
        if(frac==f.Fraction(num,den)):
            a.append(frac)
            #print('appending ',frac, num,'/',den)
#print('len(a) is',len(a))
p=f.Fraction(1,1)
for i in range(len(a)):
    p=p*a[i]
print('p is',p)