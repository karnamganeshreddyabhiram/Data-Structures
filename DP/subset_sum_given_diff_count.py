"""
Find number of ways we can partition array into 2 subsets s1 and s2. Where s1>=s2 (sums) and
s1-s2==D
a=[5,2,6,4] and D=3, we have (6,4) and (5,2) => 10-7=3

We know that,
s1+s2 = Total sum
s1 = TS - s2

s1-s2=D
TS-s2-s2=D
TS-2*s2 = D
s2 = (TS-D)/2

So we need to count the number of subsets whose sum is equals to s2
"""

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

a=[5,2,6,4]
D=3
s=sum(a)
if(s-D<=0 or (s-D)%2==1):
    print("No")
else:
    s2 = (s-D)//2
    dp=[[0 for j in range(s2+1)] for i in range(len(a))]
    print(f(s2))
