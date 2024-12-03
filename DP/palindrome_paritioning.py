"""
Minimum cuts to make a string into palidrome substrings 
"""

#Using recursion
def f(ind,n):
    if(ind==n):
        return 0
    mini=float("inf")
    for i in range(ind,n):
        if(s[ind:i+1]==s[ind:i+1][::-1]):
            cost= 1+f(i+1,n)
            mini=min(cost,mini)
    return mini

s="bababcbadcede"
ans=f(0,len(s))-1
print(ans)

#Using memorization
def f(ind,n):
    if(ind==n):
        return 0
    if(dp[ind]!=-1):
        return dp[ind]
    mini=float("inf")
    for i in range(ind,n):
        if(s[ind:i+1]==s[ind:i+1][::-1]):
            cost= 1+f(i+1,n)
            mini=min(cost,mini)
    dp[ind]=mini
    return mini

s="bababcbadcede"
dp=[-1 for i in range(len(s))]
ans=f(0,len(s))-1
print(ans)

#Using tabulation
s="bababcbadcede"
dp=[0 for i in range(len(s)+1)]
for i in range(len(s)-1,-1,-1):
    mini=float("inf")
    for ind in range(i,len(s)):
        if(s[i:ind+1]==s[i:ind+1][::-1]):
            cost=1+dp[ind+1]
            mini=min(mini,cost)
    dp[i]=mini
print(dp[i]-1)
            
            