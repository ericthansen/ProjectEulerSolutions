# Number letter counts
# Problem 17 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


#dictionary of length of words from 1 to 19

d19={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,
16:7,17:9,18:8,19:8}
#dictionary of length of words of tens - key2 is twenty, key3 is thirty, etc.
d20={2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}

def numToWordLen(x):
    if x==1000:
        return 11
    ones=x%10
    tens=(x-ones)%100//10
    hundreds=(x-tens-ones)%1000//100
    #print(hundreds,tens,ones)
    #hundreds length:
    if(hundreds==0):
        hlen=0
    else:
        hlen=d19[hundreds]+len('hundred')
    if(hundreds>0 and (tens>0 or ones>0)):
        andlen=3
    else:
        andlen=0
    if(tens==0):
        tlen=0
    elif(tens==1):
        ones=ones+tens*10
        tlen=0
    else:
        tlen=d20[tens]
    if(ones == 0):
        olen=0
    else:
        olen=d19[ones]
    #print(hlen,andlen,tlen,olen)
    #print()
    totlen=hlen+andlen+tlen+olen
    return totlen

total=0
for i in range(1,1001):
    total+=numToWordLen(i) 
print('1-1000',total)
a=5
b=99
total=0
for i in range(a,b+1):
    total+=numToWordLen(i) 
print(a,'-',b,total)
print('342',numToWordLen(342))
print('115',numToWordLen(115))
print('1+2+3+4+5',numToWordLen(1)+numToWordLen(2)+numToWordLen(3)+numToWordLen(4)+numToWordLen(5))


print('------------')
# ###or, do it by hand:
# #0-100:
# one - 9, each times 10: 360
# adjustment for teens: 34
# twenty-ninety: 46 times 10: 460
# these happen 10 times for total of : (8540)
# #the word 'hundred':
# 7 * 900 = (3600)
# #all of the ___ hundred's:
# 36 * 100 - 3600
# #the word and:
# (900-9)*3 = (2673)
# #the "one thousand"
# (11)
# = (18424)
#This is falling short of above, I am missing something, but above method works