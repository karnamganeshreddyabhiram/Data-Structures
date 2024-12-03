"""
Unbounded knapsack
An item can be taken any number of times
"""

#Using recursion
def f(ind,W):
    if(ind==0):
        return (W//w[0])*v[0] #If we reach the index 0, then lets take the item as many times as we can and each time it is v[0]
    if(W==0):
        return 0
    l = f(ind-1,W)
    r = float("-inf")
    if(W>=w[ind]):
        r = f(ind,W-w[ind])+v[ind]
    return max(l,r)

w=[2,4,6]
v=[5,11,13]
W=10
print(f(len(w)-1,W))

#Using memorization
def f(ind,W):
    if(ind==0):
        return (W//w[0])*v[0] #If we reach the index 0, then lets take the item as many times as we can and each time it is v[0]
    if(W==0):
        return 0
    if(dp[ind][W]!=-1):
        return dp[ind][W]
    l = f(ind-1,W)
    r = float("-inf")
    if(W>=w[ind]):
        r = f(ind,W-w[ind])+v[ind]
    dp[ind][W] = max(l,r)
    return dp[ind][W]

w=[2,4,6]
v=[5,11,13]
W=10
dp = [[-1 for j in range(W+1)] for i in range(len(w))]
print(f(len(w)-1,W))

#Using tabulation
def f(W):
    for i in range(W+1):
        dp[0][i] = (i//w[0])*v[0]
    for i in range(1,len(w)):
        for j in range(1,W+1):
            l = dp[i-1][j]
            r = float('-inf')
            if(j>=w[i]):
                r = dp[i][j-w[i]]+v[i]
            dp[i][j] = max(l,r)
    return dp[i][j]
w=[2,4,6]
v=[5,11,13]
W=10
dp = [[0 for j in range(W+1)] for i in range(len(w))]
print(f(W))