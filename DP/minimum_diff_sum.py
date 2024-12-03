"""
Find minimum difference of 2 subset arrays
a=[3,2,7]
[7] and [3,2]
7-5 = 2
"""

#Using tabulation
def f(target):
    dp[0][a[0]]=True
    for i in range(len(a)):
        dp[i][0]=True
    for i in range(1,len(a)):
        for j in range(1,target+1):
            l = dp[i-1][j]
            r=False
            if a[i]<=j:
                r = dp[i-1][j-a[i]]
            dp[i][j] = l or r

a=[3,2,7]
target=sum(a)
dp = [[False for j in range(target+1)] for i in range(len(a))]
f(target)
l=dp[len(a)-1]
mini=float('inf')
for i in range(len(l)-1):
    if l[i]==True:
        mini = min(mini,target-i)
print(mini)
            