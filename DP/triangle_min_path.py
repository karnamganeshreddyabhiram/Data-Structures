"""
Triangle minimum path sum
1
2 3
4 5 6
7 8 9 10
Minimum path to reach the ending line
"""

#Using recursion
def f(i,j,n):
    if(i==n-1):
        return a[n-1][j]
    l = f(i+1,j,n)+a[i][j]
    r = f(i+1,j+1,n)+a[i][j]
    return min(l,r)

a=[[1],[2,3],[4,5,6],[7,8,9,10]]
print(f(0,0,len(a)))

#Using memorization
def f(i,j,n,dp):
    if(i==n-1):
        return a[n-1][j]
    if dp[i][j]!=-1:
        return dp[i][j]
    l = f(i+1,j,n,dp)+a[i][j]
    r = f(i+1,j+1,n,dp)+a[i][j]
    dp[i][j] = min(l,r)
    return dp[i][j]

a=[[1],[2,3],[4,5,6],[7,8,9,10]]
dp = [[-1 for j in range(len(a[i]))] for i in range(len(a)) ]
print(f(0,0,len(a),dp))

#Using tabulation
def f(n,dp):
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a[i])):
            if(i==n-1):
                dp[i][j] = a[i][j]
                continue
            l = dp[i+1][j] + a[i][j]
            r = dp[i+1][j+1] + a[i][j]
            dp[i][j] = min(l,r)
    return dp[0][0]

a=[[1],[2,3],[4,5,6],[7,8,9,10]]
dp = [[-1 for j in range(len(a[i]))] for i in range(len(a)) ]
print(f(len(a),dp))
