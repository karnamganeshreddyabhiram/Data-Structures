"""
Longest common subsequence
s1 = "acd", s2 = "ced"
"cd" is the longest common subsequence
Have 2 pointers ind1 and ind2,
if at ind1 and ind2 characters are equal we can increase the count and decrease ind1 and ind2 by -1
else, once decrease ind1 and once decrease ind2  and get the maximum of both
"""

#Using recursion
def f(ind1,ind2):
    if(ind1<0 or ind2<0):
        return 0
    if(s1[ind1]==s2[ind2]):
        return 1+f(ind1-1,ind2-1)
    else:
        return max(f(ind1-1,ind2),f(ind1,ind2-1))
s1="acd"
s2="ced"
print(f(len(s1)-1,len(s2)-1))

#Using memoriztion
def f(ind1,ind2):
    if(ind1<0 or ind2<0):
        return 0
    if dp[ind1][ind2]!=-1:
        return dp[ind1][ind2]
    if(s1[ind1]==s2[ind2]):
        dp[ind1][ind2] = 1+f(ind1-1,ind2-1)
        return dp[ind1][ind2]
    else:
        dp[ind1][ind2] = max(f(ind1-1,ind2),f(ind1,ind2-1))
        return dp[ind1][ind2]

s1="acd"
s2="ced"
dp = [[-1 for j in range(len(s2))] for i in range(len(s1))]
print(f(len(s1)-1,len(s2)-1))

#Using tabulation
def f(ind1,ind2):
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[i][j]

s1="acd"
s2="ced"
dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f(len(s1),len(s2)))
                