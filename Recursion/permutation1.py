def permutation(arr,ds,freq,ans):
    if(len(ds)==len(arr)):
        x=ds.copy()
        ans.append(x)
        return
    for i in range(len(arr)):
        if not freq[i]:
            freq[i]=True
            ds.append(arr[i])
            permutation(arr, ds, freq, ans)
            ds.pop()
            freq[i]=False

arr=[1,2,3]
ds=[]
freq=[False]*len(arr)
ans=[]
permutation(arr, ds, freq, ans)
print(ans)