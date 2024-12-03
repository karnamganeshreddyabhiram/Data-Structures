"""
Minimum insertions to make a string into palindrome
s="abcaa"
Take maximum palindromic subsequence "aaa"
Now we need to insert c and b, it beomes "abca'cb'a"
So, we need to find maximum palindromic subsequence and then subtract it with string length
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
    return len(s)-dp[i][j]

s="abcaa"
print(longestPalindromeSubseq(s))