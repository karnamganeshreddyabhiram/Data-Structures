"""
Longest common substring
s1="abcdaf", s2="zbcdf"
LCS = bcd => 3
"""

def f(ind1,ind2):
    maxi=float("-inf")
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                maxi=max(maxi,dp[i][j])
    return maxi

s1="abcdaf"
s2="zbcdf"
dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f(len(s1)-1,len(s2)-1))