#Using recursion
def f(i,j):
    if(i==0 and j==0):
        return 1
    if(i<0 or j<0 or grid[i][j]==-1):
        return 0
    l = f(i-1,j)
    r = f(i,j-1)
    return l+r

n=int(input())
m=int(input())
grid = [[0,0],[-1,0]]
print(f(1,1))

#Using memorization
def f(i,j,dp):
    if(i==0 and j==0):
        return 1
    if(i<0 or j<0 or grid[i][j]==-1):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    l = f(i-1,j,dp)
    r = f(i,j-1,dp)
    dp[i][j]=l+r
    return l+r

n=int(input())
m=int(input())
dp=[[-1 for j in range(m)] for i in range(n)]
grid = [[0,0],[-1,0]]
print(f(1,1,dp))

#Using tabulation
def f(dp,n,m):
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==-1):
                dp[i][j]=0
            elif(i==0 and j==0):
                dp[i][j]=1
            else:
                up=0
                left=0
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                dp[i][j]=up+left
    return dp[n-1][m-1]

n=int(input())
m=int(input())
dp=[[-1 for j in range(m)] for i in range(n)]
grid = [[0,0],[-1,0]]
print(f(dp,n,m))