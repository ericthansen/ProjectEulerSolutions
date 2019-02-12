# Double-base palindromes
# Problem 36 
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def ispal(x):
    x=str(x)
    if(x==x[::-1]):
        return True
    else:
        return False

def main(cap):
    s=0
    for i in range(cap):
        if ispal(i) and ispal(bin(i)[2:]):
            s+=i
    print('answer is',s)

main(10**6)