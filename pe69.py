'''
Totient maximum
  Show HTML problem content  
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n/φ(n)
2   1   1   2
3   1,2 2   1.5
4   1,3 2   2
5   1,2,3,4 4   1.25
6   1,5 2   3
7   1,2,3,4,5,6 6   1.1666...
8   1,3,5,7 4   2
9   1,2,4,5,7,8 6   1.5
10  1,3,7,9 4   2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

#Note: Euler's Product Formula:
#phi(n) = n* Product_(p|n)(1-1/p)
import time

def isPrime(n) : 
  
    # Edge cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked to skip middle five numbers below 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def primeSieve(cap = 10**6 + 1):
    primestart=time.time()
    prime_d = {2:""}
    prime_l = [2]
    
    for i in range(3,cap,2):
        if isPrime(i):
            prime_d[i]=""
            prime_l.append(i)
    print('prime_dictionary finished')
    primeend=time.time()
    print('Prime Time: {}'.format(primeend-primestart))
    #print('maxprime: {}'.format(prime_l[-1]))
    #print(prime_l[0:10])
    return (prime_d,prime_l)
prime_d , prime_l = primeSieve()

def phi(n):
    #phi(n) = n* Product_(p|n)(1-1/p)
    tot = n
    i = 0
    p = prime_l[i]
    while p <= n:
        
        if n % p == 0 and p <= n:
            #print('n:{}, i:{}, p:{},tot:{}'.format(n,i,p,tot))
            #print(1-1/p)
            tot = tot * (1-(1/p))
            #print('tot:{}'.format(tot))
        i += 1
        try:
            p = prime_l[i]
        except:
            break
    return int(tot)

shortway=1
i = -1
while shortway < 10**6:
    i += 1
    shortway = shortway * prime_l[i]

shortway = shortway / prime_l[i]
print('shortway: {}; phi(shortway): {}, shortway over phi(shortway):{}'.format(shortway,phi(shortway), shortway/phi(shortway)))
'''This is another fine example of ProjectEuler describing a neat thing that appears
    to lead us to test a lot of cases,
    but actually the premise is more straightforward.  
    We did write a function to compute n/phi(n) for all n < 1 million, but
    it is necessarily faster to realize that that phi(n) is maximized when n is prime
    and phi(n) is minimized when n is composed of as many primes as possible.
    So, we just multiply increasing primes together to find the maximum product
    below 1 million.'''


phiStartTime=time.time()
answer = 0
answern = 0
for j in range(2, 10**2+1):
    if j in prime_d.keys():
        continue
        #because primes all have very high phi(n)
    nOverPhiN=j/phi(j)
    if nOverPhiN > answer:
        answer = nOverPhiN
        answern = j
    if j % 10**4 == 0:
        phiEndTime = time.time()
        print('{} out of 10**6. Elapsed time:{}'.format(j, phiEndTime-phiStartTime))
phiEndTime = time.time()
print('Phi time:{}'.format(phiEndTime-phiStartTime))
#print('Maximum n/phi(n) of {} occurs at n = {}'.format(answer, answern))


