"""
Maximum path from 1st to last row where you can move one step down or own step left diagonal
or one step right diagonal. You can start from anywhere and reach anywhere.
1 1 100
2 2 3
3 10 2
Max path if starting at 3 -> 3,2,100 = 105
Find max path from 3, 10, 2 and print the maximum
"""

#Using recursion
def f(i,j,n,m):
    if(j<=0 or j>=m):
        return float("-inf")
    if(i==0):
        return a[i][j]
    s = f(i-1,j,n,m) + a[i][j]
    l = f(i-1,j-1,n,m) + a[i][j]
    r = f(i-1,j+1,n,m) + a[i][j]
    return max(s,l,r)

a=[[1,1,100],[2,2,3],[3,10,2]]
n=len(a)
m=len(a[0])
maxi=0
for j in range(m):
    maxi=max(f(n-1,j,n,m),maxi)
print(maxi)    

#Using memorization
def f(i,j,n,m,dp):
    if(j<=0 or j>=m):
        return float("-inf")
    if(i==0):
        return a[i][j]
    if dp[i][j]!=-1:
        return dp[i][j]
    s = f(i-1,j,n,m,dp) + a[i][j]
    l = f(i-1,j-1,n,m,dp) + a[i][j]
    r = f(i-1,j+1,n,m,dp) + a[i][j]
    dp[i][j]= max(s,l,r)
    return dp[i][j]

a=[[1,1,100],[2,2,3],[3,10,2]]
n=len(a)
m=len(a[0])
maxi=0
for j in range(m):
    dp = [[-1 for j in range(m)] for i in range(n)]
    maxi=max(f(n-1,j,n,m,dp),maxi)
print(maxi)    

#Using tabulation
def f(n,m):
    for i in range(n):
        for j in range(m):
            if(i==0):
                dp[i][j]=a[i][j]
                continue
            s=0
            l=0
            r=0
            if(i>0):
                s=dp[i-1][j]
            if(i>0 and j>0):
                l=dp[i-1][j-1]
            if(i>0 and j<m-1):
                r=dp[i-1][j+1]
            dp[i][j]=max(s,l,r)+a[i][j]

a=[[1,1,100],[2,2,3],[3,10,2]]
n=len(a)
m=len(a[0])
maxi=0
dp = [[-1 for j in range(m)] for i in range(n)]
f(n,m)
for i in range(m):
    maxi=max(dp[n-1][i],maxi)
print(maxi)    

