"""
If an element is 0 then its row and column should be changed to 0s
"""
arr=[[0,0,0,1],[1,0,1,1],[1,1,0,0],[0,0,0,1]]
n=len(arr)
m=len(arr[0])
r=[-1]*n
c=[0]*m
for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            r[i]=0
            c[j]=0
for i in range(n):
    for j in range(m):
        if(r[i]==0 or c[j]==0):
            arr[i][j]=0
print(arr)