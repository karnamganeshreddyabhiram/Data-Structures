"""
Equal subset sum sets problem
Find wheather we can divide array into two subsets whose sum is equal
[1,2,3,4]
We have (2,3) and (1,4)

Find the sum of whole array and if it is odd we can't divide
if it is even, check for a subset with target sum s/2, if one part of subset sum is s/2
by default other subset sum is s/2 since whole array size is s

Check subset sum problem before this
"""

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
s=sum(a)
if(s%2):
    print("No")
else:
    dp = [[False for j in range((s//2)+1)] for i in range(len(a))]
    print(f(s//2))
