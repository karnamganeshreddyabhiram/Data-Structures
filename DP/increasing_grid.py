def f(i,j,n,m,A):
    if(i==n and j==m):
        dp[i][j]=1
        return 1
    if(dp[i][j]!=-1):
        return dp[i][j]
    l=r=0
    if(i+1<=n and A[i][j]<A[i+1][j]):
        l= 1+f(i+1,j,n,m,A)
    if(j+1<=m and A[i][j]<A[i][j+1]):
        r= 1+f(i,j+1,n,m,A)
    dp[i][j] = max(l,r)
    return dp[i][j]

A=[[1,2,3,4]]
n=len(A)-1
m=len(A[0])-1
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
ans= f(0,0,n,m,A)
print(ans)