"""
Find the number of distinct subsequences present in string s1 of string s2
s1 = babgbag
s2 = bag
"""

#Using recursion
def f(i,j):
    if j<0:
        return 1
    if i<0:
        return 0
    if(s1[i]==s2[j]):
        return f(i-1,j-1)+f(i-1,j)
    else:
        return f(i-1,j)

s1="babgbag"
s2="bag"
print(f(len(s1)-1,len(s2)-1))

#Using memorization
def f(i,j):
    if j<0:
        return 1
    if i<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if(s1[i]==s2[j]):
        dp[i][j]=f(i-1,j-1)+f(i-1,j)
        return dp[i][j]
    else:
        dp[i][j]=f(i-1,j)
        return dp[i][j]

s1="babgbag"
s2="bag"
dp=[[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f(len(s1)-1,len(s2)-1))

#Using tabulation
def f():
    for i in range(len(s2)):
        dp[0][i]=0
    for j in range(len(s1)):
        dp[j][0]=1
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[i][j]

s1="babgbag"
s2="bag"
dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f())