class Itemvalue:
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

            curwt=i.wt
            curval=i.val

            if capacity-curwt>=0:
                capacity-=curwt
                totalvalue+=curval

            else:
                fraction=capacity/curwt
                totalvalue=totalvalue+(fraction*curval)
                capacity=int(capacity-(fraction*curwt))
                break

        return totalvalue

k=Knapsack()
wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50
print(k.getmaxvalue(wt,val,capacity))








