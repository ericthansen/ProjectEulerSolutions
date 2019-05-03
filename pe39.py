# Integer right triangles

# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

#Exhaustive try:
maxsols=0
maxsolsi=0
for i in range(1,1001):
    numsolsi=0
    for c in range(int(i/3),int(i/2)+1):
        for b in range(1,c):
            isTriple=False
            a=(c**2-b**2)**(.5)
            if int(a)==a and a+b+c==i and a<b and b<c:
                isTriple=True
                #print(a,b,c)
            if isTriple:
                numsolsi+=1
    if numsolsi>maxsols:
        maxsols=numsolsi
        maxsolsi=i
        #print(i)
print('maxsolsi:',maxsolsi,'maxsols',maxsols)
