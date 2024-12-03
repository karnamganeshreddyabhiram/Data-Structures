"""
Edit distance
Find the minimum number of operations to convert s1 to s2
1) If both chars are same then i-1 and j-1
2) If we want to add some new character then i stays where it is because we adding at i+1, and j reduces to j-1
3) If we want to delete a char in s1 then i-1 and j stays at same place
4) If we want to replace with new char then i-1 and j-1
"""

#Using recursion
def f(i,j):
    if i<0:
        return j+1
    if j<0:
        return i+1
    if s1[i]==s2[j]:
        return f(i-1,j-1)
    else:
        return 1 + min(f(i-1,j), f(i,j-1), f(i-1,j-1))
s1="horse"
s2="ros"
print(f(len(s1)-1,len(s2)-1))

#Using memorization
def f(i,j):
    if i<0:
        return j+1
    if j<0:
        return i+1
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j] = f(i-1,j-1)
        return dp[i][j]
    else:
        dp[i][j] = 1 + min(f(i-1,j), f(i,j-1), f(i-1,j-1))
        return dp[i][j]
s1="horse"
s2="ros"
dp = [[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f(len(s1)-1,len(s2)-1))

#Using tabulation
def f():
    for i in range(len(s1)+1):
        dp[i][0]=i
    for j in range(len(s2)+1):
        dp[0][j]=j
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[i][j]
s1="horse"
s2="ros"
dp = [[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f())
