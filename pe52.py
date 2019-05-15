# Permuted multiples

# Problem 52
# It can be seen that the number, 125874, and its double, 251748, 
#contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
#and 6x, contain the same digits.

def check(x,y):
    s=str(x)
    t=str(y)
    if(len(s)!=len(t)):
        return False
    l=[]
    m=[]
    for i in range(len(s)):
        l.append(s[i])
    for j in range(len(t)):
        try:
            l.remove(t[j])
        except:
            return False
    return True

def main(start=1,end=10**10):
    for i in range(start,end,1):
        if(check(i,2*i)):
            if(check(i,3*i)):
                if(check(i,4*i)):
                    if(check(i,5*i)):
                        if(check(i,6*i)):
                            return i

print(main(125874))
