"""
Minimum path sum to reach end of the grid.
"""
#Using recursion
def f(i,j,n,m):
    if i==n-1 and j==m-1:
        ds.append(grid[i][j])
        print(ds)
        ds.pop()
        return grid[i][j]
    if i>=n or j>=m:
        return float('inf')
    ds.append(grid[i][j])
    l=f(i+1,j,n,m) + grid[i][j]
    r=f(i,j+1,n,m) + grid[i][j]
    ds.pop()
    return min(l,r)

ds=[]
grid=[[10,20],[30,40]]
print(f(0,0,2,2))

#Using memorization
def f(i,j,n,m,dp):
    if i==n-1 and j==m-1:
        return grid[i][j]
    if i>=n or j>=m:
        return float('inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    l=f(i+1,j,n,m,dp) + grid[i][j]
    r=f(i,j+1,n,m,dp) + grid[i][j]
    dp[i][j] = min(l,r)
    return dp[i][j]

dp=[[-1,-1],[-1,-1]]
grid=[[10,20],[30,40]]
print(f(0,0,2,2,dp))

#Using Tabulation
def f(n,m,dp):
    for i in range(n):
        for j in range(m):
            l = float('inf')
            r = float('inf')
            if i==0 and j==0:
                dp[i][j]=grid[0][0]
                continue
            if i>0:
                l=dp[i-1][j]
            if j>0:
                r=dp[i][j-1]
            dp[i][j] = min(l,r)+grid[i][j]
    return dp[n-1][m-1]

dp=[[-1,-1],[-1,-1]]
grid=[[10,20],[30,40]]
print(f(2,2,dp))