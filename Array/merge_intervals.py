"""
Merge intervals
https://leetcode.com/problems/merge-intervals/
"""
arr=[[1,3],[8,10],[2,6],[9,9],[15,18]]
arr=sorted(arr, key=lambda x:x[0])
l,r=arr[0]
ds=[]
print(arr)
for i in range(1,len(arr)):
    l1,r1=arr[i]
    if(l1<r):
        r=max(r,r1)
    else:
        ds.append([l,r])
        l=l1
        r=r1
ds.append([l,r])
print(ds)