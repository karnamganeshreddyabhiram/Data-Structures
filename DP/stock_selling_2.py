"""
Stock buy and sell any number of times. Can't buy again until you sell the previous one
Find maximum profit
"""

#Using recurssion
def f(ind,buy,n):
    if(ind==n):
        return 0
    if(buy):
        l=-v[ind]+f(ind+1,0,n)
        r=f(ind+1,1,n)
        profit=max(l,r)
    else:
        l=v[ind]+f(ind+1,1,n)
        r=f(ind+1,0,n)
        profit=max(l,r)
    return profit

v=[1,2,3,4,5,6,7]
print(f(0,1,len(v)))
        
#Using memorization
def f(ind,buy,n):
    if(ind==n):
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    if(buy):
        l=-v[ind]+f(ind+1,0,n)
        r=f(ind+1,1,n)
        profit=max(l,r)
    else:
        l=v[ind]+f(ind+1,1,n)
        r=f(ind+1,0,n)
        profit=max(l,r)
    dp[ind][buy]=profit
    return profit

v=[1,2,3,4,5,6,7]
dp=[[-1 for j in range(2)] for i in range(len(v))]
print(f(0,1,len(v)))

#Using tabulation
def f(ind,buy,n):
    dp[n][0]=0
    dp[n][1]=0
    for i in range(n-1,-1,-1):
        for j in range(2):
            if(j):
                l=-v[i]+dp[i+1][0]
                r=dp[i+1][1]
                profit=max(l,r)
            else:
                l=v[i]+dp[i+1][1]
                r=dp[i+1][0]
                profit=max(l,r)
            dp[i][j]=profit
    return dp[0][1]

v=[1,2,3,4,5,6,7]
dp=[[-1 for j in range(2)] for i in range(len(v)+1)]
print(f(0,0,len(v)))
