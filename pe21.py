# Amicable numbers
# Problem 21 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


def d(n):
    #sum of proper divisors of n
    s=1
    i=2
    while i**2<=n:
        if(n%i==0):
            j=n/i
            s+=i
            if j!=i:
                s+=j
        i+=1
    return s
print('sum of divisors of 284:',d(220))
print('sum of divisors of 220:',d(284))
#print(d(1))
ds={}
for i in range(1,10000):
    ds[i]=d(i)
#print(ds)

ams={}
for key1, val1 in ds.items():
    #nested loop obviously bad, but acceptable
    for key2,val2 in ds.items():
        if key1==val2 and key2==val1 and key1!=key2:
            ams[key1]=key1
            ams[key2]=key2
amsum=0
for k in ams.keys():
    amsum+=k
print('sum of amicable numbers under 10000:',amsum)

