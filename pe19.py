# Counting Sundays
# Problem 19 
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

dcounter=0
firstSundayCount=0
dweek={0:"M",1:"T",2:"W",3:"Th",4:"F",5:"Sa",6:"Su"}
dct={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for year in range(1900,2000+1):
    for month in range(1,12+1):
        if((year%4==0 and year%100!=0) or (year%400==0)):
            isLeap=True
        else:
            isLeap=False
        if isLeap and month==2:
            mdays=29
        else:
            mdays=dct[month]
        for day in range(1,mdays+1):
            if dweek[dcounter]=="Su" and day==1 and year>=1901:
                firstSundayCount+=1
            dcounter = (dcounter+1)%7
print("There were",firstSundayCount, "Sundays on the first of the month.")

