"""
Find the number of subsets whose sum is equals to target
a=[1,2,3,4]
(1,3) and (4)
Answer is 2
"""
#Using recursion
def f(ind,target):
    if(target==0):
        return 1
    if(ind<0):
        if(target==0):
            return 1
        return 0
    l = f(ind-1,target)
    r=0
    if(a[ind]<=target):
        r = f(ind-1,target-a[ind])
    return l+r

a=[1,2,3,4]
target=4
print(f(len(a)-1,target))

#Using memorization
def f(ind,target):
    if(target==0):
        return 1
    if(ind<0):
        if(target==0):
            return 1
        return 0
    if(dp[ind][target]!=-1):
        return dp[ind][target]
    l = f(ind-1,target)
    r=0
    if(a[ind]<=target):
        r = f(ind-1,target-a[ind])
    dp[ind][target] = l+r
    return dp[ind][target]

a=[1,2,3,4]
target=4
dp=[[-1 for j in range(target+1)] for i in range(len(a))]
print(f(len(a)-1,target))

#Using tabulation
def f(target):
    for i in range(len(a)):
        dp[i][0] = 1
    dp[0][a[0]] = 1
    for i in range(1,len(a)):
        for j in range(1,target+1):
            l = dp[i-1][j]
            r = 0
            if(a[i]<=j):
                r = dp[i-1][j-a[i]]
            dp[i][j] = l+r
    return dp[len(a)-1][target]

a=[1,2,3,4]
target=4
dp=[[0 for j in range(target+1)] for i in range(len(a))]
print(f(target))
