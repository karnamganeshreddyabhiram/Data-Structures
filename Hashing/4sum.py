"""
4 sum
Find quadraples which sums to the given target
"""

arr=[1,3,4,4,4,5,6,7,7,8,10]
t=13
arr.sort()
n=len(arr)
ans=[]
for i in range(n):
    for j in range(i+1,n):
        t1=t-arr[i]-arr[j]
        l=j+1
        r=n-1
        while(l<r):
            s=arr[l]+arr[r]
            if s<t1:
                l+=1
            elif s>t1:
                r-=1
            else:
                ds=[arr[i],arr[j],arr[l],arr[r]]
                ans.append(ds)
                while(l<r and arr[l]==ds[2]):
                    l+=1
                while(l<r and arr[r]==ds[3]):
                    r-=1
print(ans)
                    