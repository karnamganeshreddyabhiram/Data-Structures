"""
0/1 knapsack
Maximize the value of bag with capacity c with the items with weights w and values v
"""

#Using recursion
def f(ind,W):
    if(ind==0):
        if(w[0]<=W):
            return v[0]
        else:
            return 0
    l = f(ind-1,W)
    r= float('-inf')
    if(w[ind]<=W):
        r = f(ind-1,W-w[ind]) + v[ind]
    return max(l,r)

w = [3,2,5]
v = [30,40,60]
W = 6
print(f(len(w)-1,W))

#Using memorization
def f(ind,W):
    if(ind==0):
        if(w[0]<=W):
            return v[0]
        else:
            return 0
    if(dp[ind][W]!=-1):
        return dp[ind][W]
    l = f(ind-1,W)
    r= float('-inf')
    if(w[ind]<=W):
        r = f(ind-1,W-w[ind]) + v[ind]
    dp[ind][W] = max(l,r)
    return max(l,r)

w = [3,2,5]
v = [30,40,60]
W = 6
dp = [[-1 for j in range(W+1)] for i in range(len(w))]
print(f(len(w)-1,W))

#Using tabulation
def f(W):
    for i in range(w[0],W+1):
        dp[0][i]=v[0]
    for i in range(1,len(w)):
        for j in range(1,W+1):
            l = dp[i-1][j]
            r = 0
            if(w[i]<=j):
                r = dp[i-1][W-w[i]] + v[i]
            dp[i][j] = max(l,r)
    return dp[i][j]
w = [3,2,5]
v = [30,40,60]
W = 6
dp = [[0 for j in range(W+1)] for i in range(len(w))]
print(f(W))


            