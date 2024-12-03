"""
Subset sum problem
Find wheather there exists a subset whose sum is equals to target
[1,2,3,4] and target = 4
We have (1,3) and (4)
"""

#Using recursion
def f(ind,target):
    if(target==0):
        return True
    if(ind==0):
        return a[0]==target
    l = f(ind-1,target)
    r=False
    if(a[ind]<=target):
        r = f(ind-1,target-a[ind])
    return l or r

a=[1,2,3,4]
print(f(len(a)-1,4))

#Using memorization
def f(ind,target,dp):
    if(target==0):
        return True
    if(ind==0):
        return a[0]==target
    if dp[ind][target-1]!=-1:
        return dp[ind][target-1]
    l = f(ind-1,target,dp)
    r=False
    if(a[ind]<=target):
        r = f(ind-1,target-a[ind],dp)
    dp[ind][target-1] = (l or r)
    return dp[ind][target-1]

a=[1,2,3,4]
target=4
dp = [[-1 for j in range(target)] for i in range(len(a))]
print(f(len(a)-1,target,dp))

#Using tabulation
def f(target):
    dp[0][a[0]]=True
    for i in range(len(a)):
        dp[i][0]=True
    for i in range(1,len(a)):
        for j in range(1,target+1):
            l=dp[i-1][j]
            r=False
            if(a[i]<=j):
                r=dp[i-1][j-a[i]]
            dp[i][j]=l or r
    return dp[len(a)-1][target]

a=[1,2,3,4]
target=4
dp = [[False for j in range(target+1)] for i in range(len(a))]
print(f(target))
