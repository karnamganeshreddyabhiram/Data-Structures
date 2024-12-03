coins=[1,2,5,10,20,50,100,500,1000] #Addition of two consequtive coins doesn't exceed the next coin, so greedy works otherwise use DP
n=len(coins)
t=226
ans=0
ds=[]
for i in range(n-1,-1,-1):
    while(t>=coins[i]):
        t-=coins[i]
        ds.append(coins[i])
        ans+=1
print(ans,ds)