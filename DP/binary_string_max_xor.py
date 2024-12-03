def lcs(n, m) : 
    maxi=0
    for i in range(n + 1) :
        for j in range(m + 1) :
            if (i == 0 or j == 0) :
                dp[i][j] = 0;
            elif (s1[i - 1] == s2[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
                maxi=max(maxi,dp[i][j])
            else :
                dp[i][j] = 0
    return maxi

s1=input()
s2=input()
s1=str(s1)
s2=str(s2)
n=len(s1)
m=len(s2)
dp = [[0 for i in range(m+1)] for i in range(n+1)]
print(lcs(n,m))