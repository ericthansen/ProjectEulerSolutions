# Coded triangle numbers

# Problem 42
# The nth term of the sequence of triangle numbers is given by, 
#tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to 
#its alphabetical position and adding these values we form a word value. 
#For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the 
#word value is a triangle number then we shall call the word a triangle 
#word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K 
#text file containing nearly two-thousand common English words, how 
#many are triangle words?

def alph(s):
    return ord((s.upper()))-64

def makeTri(n):
    trilist=[]
    for i in range(1,n+1):
        trilist.append(int(1/2*i*(i+1)))
    return trilist
myTri=makeTri(10000)#chosen sufficiently large

def isTri(x,myTri):
    if x in myTri:
        return True
    else:
        return False


words=open('/Users/ehansen/Desktop/CompSci/ProjectEuler/p042_words.txt')
s=str(words.readline())
wordlist=s.split(',')
countTri=0
for word in wordlist:
    w=word.strip("\"")
    value=0
    for i in range(len(w)):
        letter=w[i]
        value+=alph(letter)
    if(isTri(value,myTri)):
        countTri+=1
print("answer:",countTri,'triangle words in the text file')
words.close()