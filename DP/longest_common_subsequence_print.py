"""
Longest common subsequence
s1 = "acd", s2 = "ced"
"cd" is the longest common subsequence
Have 2 pointers ind1 and ind2,
if at ind1 and ind2 characters are equal we can increase the count and decrease ind1 and ind2 by -1
else, once decrease ind1 and once decrease ind2  and get the maximum of both
"""

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
n=f(len(s1),len(s2))
print(dp)                
ans=""
for i in range(n):
    ans+="$"
i=len(s1)
j=len(s2)
index=n-1
while(i>0 and j>0):
    if(s1[i-1]==s2[j-1]):
        ans=ans[:index]+s1[i-1]+ans[index+1:]
        i-=1
        j-=1
        index-=1
    else:
        if(dp[i-1][j]>dp[i][j-1]):
            i-=1
        else:
            j-=1
print(ans)
        