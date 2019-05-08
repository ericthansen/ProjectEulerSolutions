# Self powers

# Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def term10(x):
    tot=1
    for i in range(1,x+1):
        tot=(tot*x)%(10**10)
    return tot%(10**10)

tot=0
for i in range(1,1001):
    tot+=term10(i)
print('The answer is:',tot%(10**10))