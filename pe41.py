# Pandigital prime

# Problem 41
# We shall say that an n-digit number is pandigital if it makes 
#use of all the digits 1 to n exactly once. For example, 2143 is a 
#4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?
#warning- this is extremely inefficient.  probably better to create pandigs and then test if prime?
def isPan(n):
    s=str(n)
    l=len(s)
    x=[]
    for i in range(1,l+1):
        x.append(i)
    for i in range(len(s)):
        if int(s[i]) in x:
            x.remove(int(s[i]))
        else:
            return False
    return True

# def primesieve(x):
#     primes=[] #empty list
#     #primeCount=0
#     candidateList=[None]*(x+1) #list with (x+1) entries all currently [None]
#     ind=0 #index to progress through candidateList
#     for j in candidateList:
#         candidateList[ind]=ind #populates candidateList with integers between 0 and x - NOTE: First Index of a List is 0!!!
#         ind+=1 #python shorthand to increment ind; i.e. ind = ind + 1
#     candidateList[1]=0 #sets 1 as "not prime"; using convention of "0" meaning not prime
#     #print(candidateList)
#     for i in range(2,x+1,1): #iterate from 2 through x by 1
#         if(candidateList[i]==0): #if our current candidate has already been identified as not prime
#             pass
#         else:#our current candidate is prime
#             primes.append(i) #add current candidate to list of primes
#             #primeCount= primeCount + 1
#             for j in range(2*i,x+1,i): #mark all multiples of current candidate as not prime
#                 candidateList[j]=0
#     print('Primes <=',x,'are',primes)# print final list of primes
#     #print('Primes found: ',primeCount)
#     return primes
# #print(isPan(132))

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
#print(isPrime(2143))

#987654321 
for i in range(987654321,1,-2):
    if(i%111111==0):
        print(i)
    if isPan(i):
        if(isPrime(i)):
            print("answer:",i)
            break