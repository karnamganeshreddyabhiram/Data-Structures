"""
Maximum sum of non adjacent elements
1,2,4 -> 6 (1,4)
"""

#Using recursion
def f(n,v):
    if(n==0):
        return v[n]
    if(n<0):
        return 0
    #If you pick, then u can't pick n-1 so n-2
    l = v[n]+f(n-2,v)
    #If you don't pick, simply go n-1
    r = f(n-1,v)
    return(max(l,r))

n=2
v=[1,2,4]
print(f(n,v))

#Using memoization
def f(n,v,dp):
    if(n==0):
        return v[n]
    if(n<0):
        return 0
    if dp[n]!=-1:
        return dp[n]
    #If you pick, then u can't pick n-1 so n-2
    l = v[n]+f(n-2,v,dp)
    #If you don't pick, simply go n-1
    r = f(n-1,v,dp)
    dp[n]=max(l,r)
    return(dp[n])

n=2
v=[1,2,4]
dp = [-1]*(n+1)
print(f(n,v,dp))

#Using tabulation
def f(n,v,dp):
    dp[0]=v[0]
    for i in range(1,n+1):
        if i>1:
            dp[i]=max(dp[i-2]+v[i],dp[i-1])
        else:
            dp[i]=v[i]
    return(dp[n])

n=2
v=[1,2,4]
dp = [-1]*(n+1) 
print(f(n,v,dp))
