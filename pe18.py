# Maximum path sum I
# Problem 18 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

#EH: I'm inclined to use dijkstra's algorithm on this.  Let's see...
#So, let's use the implementation I came up with to teach last year.

#importing weights:
wts=[[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
cap=1000
for i in range(len(wts)):
    for j in range(len(wts[i])):
            wts[i][j]= cap-wts[i][j]
#print(wts)

import copy
import random
import hashlib
import math


class vertex():
    def __init__(self,nameIn="",eWeightIn=0):
        self.edgelist=[]
        self.tweight=float("inf")
        self.entryWeight=eWeightIn
        self.name=nameIn
        self.prev=None
        #self.visited=False

    def addEdge(self,edgeIn):
        self.edgelist.append(edgeIn)

    def refreshWeight(self,weightIn):
        if(self.tweight>weightIn):
            self.tweight=weightIn

    def resetWeight(self):
        self.tweight=float("inf")
    
    def resetPrev(self):
        self.prev=None

    def __repr__(self):
        return self.name

class edge():
    def __init__(self,weightin=0,v1in=None,v2in=None):
        self.weight=weightin
        self.v1=v1in
        self.v2=v2in

    def setWeight(self,weightin):
        self.weight=weightin

    def setV1(self,vin):
        self.v1=vin

    def setV2(self,vin):
        self.v2=vin

    def getOtherV(self,vIn): #new added - gives vertices ability to access neighbor vertices through a connected edge
        if(vIn==self.v1):
            return self.v2
        elif(vIn==self.v2):
            return self.v1
        else:
            return None

class graph():
    def __init__(self):
        self.vertexList=[]
        #self.edgeList[]

    def isEmpty(self):
        if len(self.vertexList)==0:
            return True
        else:
            return False

    def addV(self, vin=None,name="",eWeightIn=0):
        if(vin==None):
            vin=vertex(nameIn=name,eWeightIn=eWeightIn)

        self.vertexList.append(vin)
        return vin

    def remove(self,vin):
        self.vertexList.remove(vin)

    def connect(self,v1in,v2in,weightIn):
        newedge=edge(weightIn,v1in,v2in)
        v1in.addEdge(newedge)
        v2in.addEdge(newedge)

    def nextcurr(self):
        if(len(self.vertexList)<=0):
            return None
        else:
            curr=self.vertexList[0]
            currweight=curr.tweight
            for j in self.vertexList:
                if j.tweight<currweight:
                    curr=j
                    currweight=j.tweight
            return curr

def randGraph(size=10,completeness=0.5, weightmax=10, weightmin=1):
    gr=graph()
    dic=dict()
    for i in range(size):
        new=vertex()
        rname="v"+str(i)
        new.name=rname
        #print(rname)
        dic[rname]=new
        #print(dic[rname])
        gr.addV(new)

    for j in range(size):
        curr=dic["v"+str(j)]
        for n in range(j+1,size):            
            if(random.random()<completeness):
                #print('weightmax is',weightmax)
                tempweight=math.ceil(random.random()*(weightmax-weightmin+1))+weightmin-1
                print(tempweight)
                gr.connect(curr,dic["v"+str(n)],tempweight)
    return gr

#note normally dijkstra finds path of least length, we look for greatest...necessary to make changes with variables 'cap' and 'worst' above and below
def dijkstra(graphIn,startv):
    for j in graphIn.vertexList:
        j.resetWeight()
        j.resetPrev()
    unvis=graph()
    unvis.vertexList=copy.copy(graphIn.vertexList)
    curr=startv
    startv.tweight=0
    while unvis.isEmpty() != True:
        #print('size',len(unvis.vertexList))
        for l in curr.edgelist :
            nbr=l.getOtherV(curr)
            #print('nbr is',nbr)
            curredgeweight=l.weight
            if (curr.tweight+curredgeweight < nbr.tweight):
                nbr.tweight=curr.tweight + curredgeweight
                nbr.prev=curr
        unvis.remove(curr)
        curr=unvis.nextcurr()

def graphTraverse(graphIn, destV):
    path=[]
    path.append(destV)
    prev=destV.prev
    print(prev)
    #print('enteringwhile')
    while prev != None:
        path.append(prev)
        prev = prev.prev
        print(prev)
    #print('exited while1')
    path.reverse()
    print("Optimal path")
    worst=-2
    for i in path:
        worst+=1
        print(i.name,cap-i.entryWeight)
    #print('exited for1')
    print('reaches',destV.name,'in',worst*cap-destV.tweight,'units.')
    return path

def main():
    myg=graph()
    root=myg.addV(name="root")
    d={'d':root}
    for row in range(len(wts)):
        for col in range(len(wts[row])):
            temp=myg.addV(name=str(row)+'_'+str(col),eWeightIn=wts[row][col])
            d[str(row)+'_'+str(col)]=temp
    goal=myg.addV(name='goal')
    d['goal']=goal

    myg.connect(d['d'],d['0_0'],d['0_0'].entryWeight)
    for row in range(len(wts)-1):
        for col in range(len(wts[row])):
            myg.connect(d[str(row)+'_'+str(col)],d[str(row+1)+'_'+str(col)],d[str(row+1)+'_'+str(col)].entryWeight)
            myg.connect(d[str(row)+'_'+str(col)],d[str(row+1)+'_'+str(col+1)],d[str(row+1)+'_'+str(col+1)].entryWeight)
    for col in range(len(wts[row+1])):
        myg.connect(d[str(row+1)+'_'+str(col)],d['goal'],0)
    print('connected')
    dijkstra(myg,d['d'])
    print('dijkstra complete')
    path=graphTraverse(myg,d['goal'])
    print('graphTraverse complete')

main()

