# #pe 75
# Singular integer right triangles
   
# Problem 75
# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

#####
#We will attempt to create primitive Pythagorean Triples (PTs) using Euclid's Formula, then create all multiples of these primitives under the ceiling value 

# When m and n are any two positive integers (m > n):

# a = m**2 − n**2
# b = 2mn
# c = m**2 + n**2
# Then a, b, and c form a Pythagorean Triple

#####
# since a**2 + b**2 == m**4+n**4-2*m**2*n**2 + 4*m**2*n**2 == m**4 + n**4 + 2*m**2*n**2 ==c**2

#other triples may be formed with side lengths k*a, k*b, k*c

L=int(1.5*10**6)

def count_unique_triples(cap):
    d={}
    count=0
    for m in range(1,int(cap**0.5+1)):
        if(m%100==0):
            print("progress - m:",m)
            
        for n in range(1,m):
            a=m**2-n**2
            b=2*m*n
            c=m**2+n**2
            k=1
            while k*(a+b+c)<=cap:
            #finding multiples
                try:
                    y=d[k*(a+b+c)]
                    if sorted([k*a,k*b,k*c]) in y:
                        pass
                    else:
                        d[k*(a+b+c)].append(sorted([k*a,k*b,k*c]))

                    #print('appending')
                except:
                    d[k*(a+b+c)]=[sorted([k*a,k*b,k*c])]
                    #print('inserting')
                k+=1

    #print(d)
    for key, val in d.items():
        if len(val)==1 and key<=int(cap):
            count+=1
    print('Solution:', count)
    print('checking max keys:',max(d.keys()))
    #print('1500000',d[1500000])
    #try:
    #    print('20',d[20])
    #except:
    #    print('20 has no such triples')
    #print('120',d[120])
    #print('40',d[40])

count_unique_triples(L)

