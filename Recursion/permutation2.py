def permutation(ans,arr,ind):
    if(ind==len(arr)):
        x=arr.copy()
        ans.append(x)
        return
    for i in range(ind,len(arr)):
        arr[i],arr[ind]=arr[ind],arr[i]
        permutation(ans, arr, ind+1)
        arr[i],arr[ind]=arr[ind],arr[i]
ans=[]
arr=[1,2,3]
ind=0
permutation(ans, arr, ind)