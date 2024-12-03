"""
Merge two sorted arrays as two arrays
arr1=[3,5,8,10]
arr2=[4,20,30,40]
After mergining
arr1=[3,4,5,8]
arr2=[10,20,30,40]
"""

#Method 1, time compleity n and space compleity n
i=0
j=0
arr1=[3,5,8,10]
arr2=[4,20,30,40]
n=len(arr1)
m=len(arr2)
arr3=[]
while(i<n and j<m):
    if arr1[i]<arr2[j]:
        arr3.append(arr1[i])
        i+=1
    else:
        arr3.append(arr2[j])
        j+=1
while(i<n):
    arr3.append(arr1[i])
    i+=1
while(j<m):
    arr3.append(arr2[j])
    j+=1
arr1=arr3[:n]
arr2=arr3[n:]
print(arr1,arr2)

#Method 2 time complexity nlogn and space complexity 1
#https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/
i=0
j=0
arr1=[3,5,8,10]
arr2=[4,20,30,40]
n=len(arr1)
m=len(arr2)
k=n-1
while(i<=k and j<m):
    if(arr1[i]<arr2[j]):
        i+=1
    else:
        arr2[j],arr1[k]=arr1[k],arr2[j]
        k-=1
        j+=1
arr1.sort()
arr2.sort()
print(arr1,arr2)