"""
Longest palindromic subsequence
s="agbdba"
"abdba" is longest palindromic subsequence
"""
def longestPalindromeSubseq( s: str) -> int:
    s1 = s[::-1]
    ind1=len(s)
    ind2=len(s1)
    dp=[[0 for j in range(ind2+1)] for i in range(ind1+1)]
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if(s[i-1]==s1[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[i][j]

s="agbdba"
print(longestPalindromeSubseq(s))