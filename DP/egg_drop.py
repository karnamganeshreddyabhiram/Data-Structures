def f(n,k):
    if(k<=1 or n==1):
        return k
    if(dp[n][k]!=-1):
        return dp[n][k]
    mini=float("inf")
    for i in range(1,k+1):
        l=f(n-1,i-1)
        r=f(n,k-i)
        mini=min(mini,max(l,r))
    dp[n][k]=mini+1
    return mini+1

n=2
k=100
dp=[[-1 for j in range(k+1)] for i in range(n+1)]
print(f(n,k))
    

dp = [[0 for j in range(k+1)] for i in range(n+1)]
for j in range(k+1):
    dp[1][j]=j
for i in range(n+1):
    dp[i][1]=1
for i in range(2,n+1):
    for j in range(2,k+1):
        mini=float("inf")
        for k in range(1,j+1):
            l=dp[i-1][k-1]
            r=dp[i][j-k]
            mini=min(mini,max(l,r))
        dp[i][j]=mini+1
print(dp[i][j])

        
