#Using recursion
def f(i,j):
    if(i==j):
        return 0
    mini=float('inf')
    for k in range(i,j):
        steps = A[i-1]*A[k]*A[j] + f(i,k)+f(k+1,j)
        mini=min(mini,steps)
    return mini

A=[10,20,30,40]
print(f(1,len(A)-1))

#Using memorization
def f(i,j):
    if(i==j):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    ans=float('inf')
    for k in range(i,j):
        steps=A[i-1]*A[k]*A[j] + f(i,k) +f(k+1,j)
        ans=min(ans,steps)
    dp[i][j]=ans
    return dp[i][j]

A=[10,20,30,40]
dp=[[-1 for j in range(len(A))] for i in range(len(A))]
print(f(1,len(A)-1))

#Using tabulation
def f(i,j):
    n=len(A)
    for i in range(n):
        dp[i][i]=0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):        
            ans=float('inf')
            for k in range(i,j):
                steps=A[i-1]*A[k]*A[j] + dp[i][k] +dp[k+1][j]
                ans=min(ans,steps)
            dp[i][j]=ans
    return dp[1][n-1]

A=[10,20,30,40]
dp=[[0 for j in range(len(A))] for i in range(len(A))]
print(f(1,len(A)-1))