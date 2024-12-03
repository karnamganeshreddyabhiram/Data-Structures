"""
Minimum number of insertions and deletions to convert one string to another
s1="abcdaf", s2="zbcdf"
LCS = bcd => 3
Delete aaf from s1 and insert zf
"""

def f(ind1,ind2):
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[i][j]

s1="abcdaf"
s2="zbcdf"
dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
n=f(len(s1)-1,len(s2)-1)
print("Minimum deletions: ",len(s1)-n)
print("Minimum insertions: ",len(s2)-n)
print("Minimum insertions and deletions",len(s1)+len(s2)-2*n)