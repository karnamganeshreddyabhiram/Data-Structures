def f(i,j):
    if(i<0 or j<0):
        return 0
    if(i==0 and j==0):
        return 1
    l=0
    if(i>=0 and arr[i-1][j]<arr[i][j]):
        l=f(i-1,j)+1
    r=0
    if(j>=0 and arr[i][j-1]<arr[i][j]):
        r=f(i,j-1)+1
    return max(l,r)

arr=[[1, 2, 3, 4 ],
    [2, 2, 3, 4 ],
    [3, 2, 3, 4 ],
    [4, 5, 6, 7 ]]
n=len(arr)
m=len(arr[0])
print(f(n-1,m-1))

def f(i,j):
    if(i<0 or j<0):
        return 0
    if(i==0 and j==0):
        return 1
    if(dp[i][j]!=-1):
        return dp[i][j]
    l=0
    if(i>0 and arr[i-1][j]<arr[i][j]):
        l=f(i-1,j)+1
    r=0
    if(j>0 and arr[i][j-1]<arr[i][j]):
        r=f(i,j-1)+1
    dp[i][j]=max(l,r)
    return max(l,r)

arr=[[1, 2, 3, 4 ],
    [2, 2, 3, 4 ],
    [3, 2, 3, 4 ],
    [4, 5, 6, 7 ]]
n=len(arr)
m=len(arr[0])
dp=[[-1 for j in range(m)] for i in range(n)]
print(f(n-1,m-1))


def f(n,m):
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                continue
            l=0
            r=0
            if(i>0 and arr[i][j]>arr[i-1][j]):
                l=dp[i-1][j]+1
            if(j>0 and arr[i][j]>arr[i][j-1]):
                r=dp[i][j-1]+1
            dp[i][j]=max(l,r)
    return dp[i][j]
    
arr=[[1, 2, 3, 4 ],
    [2, 2, 3, 4 ],
    [3, 2, 3, 4 ],
    [4, 5, 6, 7 ]]
n=len(arr)
m=len(arr[0])
dp=[[0 for j in range(m)] for i in range(n)]
print(f(n,m))