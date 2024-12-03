"""
Maximum rain water stored
At a given index, the amount of water stored = min(max(left)+max(right))-a[i]
"""

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(arr)
l=[0]*n
r=[0]*n

l[0]=arr[0]
for i in range(1,n):
    if arr[i]>l[i-1]:
        l[i]=arr[i]
    else:
        l[i]=l[i-1]

r[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    if arr[i]>r[i+1]:
        r[i]=arr[i]
    else:
        r[i]=r[i+1]
        
ans=0
for i in range(n):
    ans+=min(l[i],r[i])-arr[i]
print(ans)

#2 pointer approach
l=0
r=n-1
maxl=0
maxr=0
ans=0
while(l<r):
    if arr[l]<=arr[r]:
        if arr[l]>=maxl:
            maxl=arr[l]
        else:
            ans+=maxl-arr[l]
        l+=1
    else:
        if arr[r]>=maxr:
            maxr=arr[r]
        else:
            ans+=maxr-arr[r]
        r-=1
print(ans)