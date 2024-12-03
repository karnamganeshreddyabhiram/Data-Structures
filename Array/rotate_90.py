"""
Rotate image
1) Transpose
2) Reverse each row
"""

arr=[[1,2,3],[4,5,6],[7,8,9]]
n=len(arr)
m=len(arr[0])
for i in range(n):
    for j in range(i):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
for i in range(n):
    for j in range(m//2):
        arr[i][j],arr[i][m-j-1]=arr[i][m-j-1],arr[i][j]
print(arr)