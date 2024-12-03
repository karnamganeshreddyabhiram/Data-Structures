def subsequences(arr,i,n,ds):
    if i>=n:
        print(ds)
        return
    ds.append(arr[i])
    subsequences(arr, i+1, n, ds)
    ds.pop()
    subsequences(arr, i+1, n, ds)

arr=[1,2,3,4]
n=len(arr)
ds=[]
i=0
subsequences(arr, i, n, ds)