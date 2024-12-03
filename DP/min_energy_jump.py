"""
Frog jump, minimum energy requried to reach the end. It can jump one step or two steps at a
time. in each jump the energy consumed = abs(current element- jumping element)
"""

#Using Recusion
def frog(n,v):
    if(n==0):
        return 0
    l = frog(n-1,v) + abs(v[n]-v[n-1])
    r = float('inf')
    if(n>1):
        r = frog(n-2,v) + abs(v[n]-v[n-2])
    return min(l,r)

v=[30,10,60,10,60,50]
n=5
print(frog(n,v))

#Using memorization
def frog(n,v,dp):
    if(n==0):
        return 0
    if dp[n]!=-1:
        return dp[n]
    l = frog(n-1,v,dp) + abs(v[n]-v[n-1])
    r = float('inf')
    if(n>1):
        r = frog(n-2,v,dp) + abs(v[n]-v[n-2])
    dp[n]=min(l,r)
    return dp[n]

v=[30,10,60,10,60,50]
n=5
dp=[-1]*(n+1)
print(frog(n,v,dp))

#Using Tabulation
def frog(n,v,dp):
    dp[0]=0
    for i in range(1,n+1):
        l=dp[i-1]+abs(v[i]-v[i-1])
        r=float('inf')
        if i>1:
            r=dp[i-2]+abs(v[i]-v[i-2])
        dp[i]=min(l,r)
    return dp[n]
v=[30,10,60,10,60,50]
n=5
dp=[-1]*(n+1)
print(frog(n,v,dp))

