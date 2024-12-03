"""
Minimum number of coins required to make the sum v (repetation of coins is allowed)
a=[3,4,6,5] and v=11
Minimum coins is 2 (6,5)
"""

#Using recursion
def f(ind,W):
    if(ind==0):
        if(W%w[0]==0):
            return W//w[0]
        else:
            return float("inf")
    if(W==0):
        return 0
    l = f(ind-1,W)
    r = float("inf")
    if(w[ind]<=W):
        r = 1+f(ind,W-w[ind])
    return min(l,r)

w=[1,3,4,6,5]
W=11
print(f(len(w)-1,W))

#Using memorization
def f(ind,W):
    if(ind==0):
        if(w[0]%W==0):
            return w[0]//W
        else:
            return float("inf")
    if(W==0):
        return 0
    if(dp[ind][W]!=-1):
        return dp[ind][W]
    l = f(ind-1,W)
    r = float("inf")
    if(w[ind]<=W):
        r = 1+f(ind,W-w[ind])
    dp[ind][W] = min(l,r)
    return dp[ind][W]

w=[1,3,4,6,5]
W=11
dp = [[-1 for j in range(W+1)] for i in range(len(w))]
print(f(len(w)-1,W))

#Using tabulation
def f(W):
    for i in range(1,W+1):
        if(w[0]%i==0):
            dp[0][i]=w[0]//i
        else:
            dp[0][i]=float("inf")
    for i in range(1,len(w)):
        for j in range(1,W+1):
            l = dp[i-1][j]
            r = float("inf")
            if(w[i]<=j):
                r = dp[i][j-w[i]]+1
            dp[i][j] = min(l,r)
    return dp[i][j]
w=[1,3,4,6,5]
W=11
dp = [[0 for j in range(W+1)] for i in range(len(w))]
print(f(W))