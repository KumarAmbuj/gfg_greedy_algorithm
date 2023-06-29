class Itemvalue():
    def __init__(self,wt,val,i):
        self.wt=wt
        self.val=val
        self.ind=i
        self.cost=val/wt

    def __lt__(self,other):
        return self.cost<other.cost

class Knapsack():

    def getmaxvalue(self,wt,val,capacity):

        totalvalue=0

        ival=[]

        for i in range(len(wt)):
            ival.append(Itemvalue(wt[i],val[i],i))

        ival.sort(reverse=True)

        for i in ival:
            print(i.cost,end=' ')

        for i in ival:

            curwt=i.wt
            curval=i.val

            if capacity-curwt>=0:
                capacity=capacity-curwt
                totalvalue=totalvalue+curval

            else:
                fraction = capacity / curwt
                totalvalue += curval * fraction
                capacity = int(capacity - (curwt * fraction))
                break
        return totalvalue

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50
k=Knapsack()
print(k.getmaxvalue(wt,val,capacity))


