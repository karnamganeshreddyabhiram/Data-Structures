"""
Rod cutting problem
Value for each length
a=[2,5,7,8,10]
Length = 5
Divide the rod so that value becomes maximum
1,1,2 => 2+2+5 = 12
2,3 => 5+7 = 12
"""
#Using recursion
def f(ind,W):
    if ind==0:
        return w[0]*W
    if(W==0):
        return 0
    l = f(ind-1,W)
    r = float("-inf")
    if W>=ind+1:
        r = w[ind]+f(ind,W-ind-1)
    return max(l,r)

w=[2,5,7,8,10]
print(f(len(w)-1,len(w)))

#Using memorization
def f(ind,W):
    if ind==0:
        return w[0]*W
    if dp[ind][W]!=-1:
        return dp[ind][W]
    if(W==0):
        return 0
    l = f(ind-1,W)
    r = float("-inf")
    if W>=ind+1:
        r = w[ind]+f(ind,W-ind-1)
    dp[ind][W] = max(l,r)
    return dp[ind][W]

w=[2,5,7,8,10]
dp = [[-1 for j in range(len(w)+1)] for i in range(len(w))]
print(f(len(w)-1,len(w)))

#Using tabulation
def f(W):
    for i in range(W+1):
        dp[0][i] = w[0]*i
    for i in range(1,len(w)):
        for j in range(1,W+1):
            l = dp[i-1][j]
            r = float("-inf")
            if(j>=i+1):
                r = dp[i][j-i-1]+w[i]
            dp[i][j] = max(l,r)
    return dp[i][j]
w=[2,5,7,8,10]
dp = [[0 for j in range(len(w)+1)] for i in range(len(w))]
print(f(len(w)))