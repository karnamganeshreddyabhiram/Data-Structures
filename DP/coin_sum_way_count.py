def f(ind,W):
    if(ind==0):
        return W%w[0]==0
    if(W==0):
        return 1
    l = f(ind-1,W)
    r = 0
    if(w[ind]<=W):
        r = f(ind,W-w[ind])
    return l + r

w=[1,1,2]
W=2
print(f(len(w)-1,W))


def f(ind,W):
    if(ind==0):
        return W%w[0]==0
    if(W==0):
        return 1
    if(dp[ind][W]!=-1):
        return dp[ind][W]
    l = f(ind-1,W)
    r = 0
    if(w[ind]<=W):
        r = f(ind,W-w[ind])
    dp[ind][W] = l+r
    return dp[ind][W]

w=[1,1,2]
W=2
dp = [[-1 for j in range(W+1)] for i in range(len(w))]
print(f(len(w)-1,W))

def f(W):
    for i in range(W+1):
        dp[0][i] = int(W%w[0]==0)
    for i in range(len(w)):
        dp[i][0] = 1
    for i in range(1,len(w)):
        for j in range(1,W+1):
            l = dp[i-1][j]
            r = 0
            if(j>=w[i]):
                r = dp[i][j-w[i]]
            dp[i][j] = l+r
    return dp[i][j]

w=[1,1,2]
W=2
dp = [[0 for j in range(W+1)] for i in range(len(w))]
print(f(W))
