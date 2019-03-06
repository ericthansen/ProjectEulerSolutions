import random

def statGen5d4Aug(numstats=6,minval=8, maxval=16,mod=2):
    raw=[]
    final=[]
    for _ in range(numstats):
        x=random.randint(1,4)+random.randint(1,4)+random.randint(1,4)+random.randint(1,4)+random.randint(1,4)
        raw.append(x)
        if(x<minval):
            x+=mod
        if(x>maxval):
            x-=mod
        final.append(x)
    print("Raw rolls:",raw,'; sum:',sum(raw))
    print("Adjusted Stats:",final,'; sum:',sum(final))
statGen5d4Aug()