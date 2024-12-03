"""
Stock selling, you can make atmost 2 transactions.
Find maximum profit
"""

#Using recursion
def f(ind,buy,c,n):
    if(c==0):
        return 0
    if(ind==n):
        return 0
    if(buy):
        l=-v[ind]+f(ind+1,0,c,n)
        r=f(ind+1,1,c,n)
        profit=max(l,r)
    else:
        l=v[ind]+f(ind+1,1,c-1,n)
        r=f(ind+1,0,c,n)
        profit=max(l,r)
    return profit

v=[3,3,5,0,3,1,4]
print(f(0,1,2,len(v)))

#Using memorization
def f(ind,buy,c,n):
    if(c==0):
        return 0
    if(ind==n):
        return 0
    if dp[ind][buy][c]!=-1:
        return dp[ind][buy][c]
    if(buy):
        l=-v[ind]+f(ind+1,0,c,n)
        r=f(ind+1,1,c,n)
        profit=max(l,r)
    else:
        l=v[ind]+f(ind+1,1,c-1,n)
        r=f(ind+1,0,c,n)
        profit=max(l,r)
    dp[ind][buy][c]=profit
    return profit

v=[3,3,5,0,3,1,4]
dp=[[[-1 for k in range(3)] for j in range(2)] for i in range(len(v))]
print(f(0,1,2,len(v)))

#Using tabulation
def f(buy,c,n):
    for i in range(n):
        for j in range(buy):
            dp[i][j][0]=0
    for i in range(buy):
        for j in range(c):
            dp[n][i][j]=0
    for i in range(n-1,-1,-1):
        for j in range(buy):
            for k in range(1,c):
                if(j):
                    l=-v[i]+dp[i+1][0][k]
                    r=dp[i+1][1][k]
                    profit=max(l,r)
                else:
                    l=v[i]+dp[i+1][1][k-1]
                    r=dp[i+1][0][k]
                    profit=max(l,r)
                dp[i][j][k]=profit
    return dp[0][1][2]
            
v=[3,3,5,0,3,1,4]
dp=[[[-1 for k in range(3)] for j in range(2)] for i in range(len(v)+1)]
print(f(2,3,len(v)))
