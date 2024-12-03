"""
Search in row wise sorted 2D grid using binary search
"""
a=[[1,2,3],[4,5,6],[7,8,9]]
n=len(a)
m=len(a[0])
i=0
j=n*m-1
k=4
while(i<=j):
    mid=(i+(j-i)//2)
    if(a[mid//m][mid%m]==4):
        print("Yes")
        break
    if(a[mid//m][mid%m]<k):
        i=mid+1
    else:
        j=mid-1
