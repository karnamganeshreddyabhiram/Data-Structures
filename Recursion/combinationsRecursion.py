#Find all possible combinations of the array elements to get target sum (Repetation allowed)
def combinations(ind,a,target,ans,ds):
    if ind==len(a):
        if(target==0):
            x=ds.copy()
            ans.append(x)
        return
    if(a[ind]<=target):
        ds.append(a[ind])
        combinations(ind,a,target-a[ind],ans,ds)
        ds.pop()
    combinations(ind+1,a,target,ans,ds)

ans=[]
a=[1,2,3]
target=4
ind=0
ds=[]
combinations(ind,a,target,ans,ds)
print(ans)