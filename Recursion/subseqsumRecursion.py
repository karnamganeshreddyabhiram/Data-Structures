#Print all the sub sequences whose is equals to target
def subseqsum(arr,ds,i,sum,n,target):
    if(i>=n):
        if(sum==target):
            print(ds)
        return
    ds.append(arr[i])
    sum+=arr[i]
    subseqsum(arr, ds, i+1,sum, n, target)
    sum-=arr[i]
    ds.pop()
    subseqsum(arr, ds, i+1, sum, n, target)

arr=[1,2,2,2,3,4]
target=3
i=0
sum=0
ds=[]
n=len(arr)
subseqsum(arr, ds, i, sum, n, target)

#Find wheather there exists a sub sequence whose sum is equals to target
def subseqsum(arr,ds,i,sum,n,target):
    if(i>=n):
        if(sum==target):
            return True
        return False
    ds.append(arr[i])
    sum+=arr[i]
    if(subseqsum(arr, ds, i+1,sum, n, target)):
        return True
    sum-=arr[i]
    ds.pop()
    if(subseqsum(arr, ds, i+1, sum, n, target)):
        return True
    return False

arr=[1,2,2,2,3,4]
target=3
i=0
sum=0
ds=[]
n=len(arr)
print(subseqsum(arr, ds, i, sum, n, target))

#Count number of subsequences whose sum is equals to target
def subseqsum(arr,ds,i,sum,n,target):
    if(i>=n):
        if(sum==target):
            return 1
        return 0
    ds.append(arr[i])
    sum+=arr[i]
    l=subseqsum(arr, ds, i+1,sum, n, target)
    sum-=arr[i]
    ds.pop()
    r=subseqsum(arr, ds, i+1, sum, n, target)
    return l+r

arr=[1,2,3,4]
target=3
i=0
sum=0
ds=[]
n=len(arr)
print(subseqsum(arr, ds, i, sum, n, target))
