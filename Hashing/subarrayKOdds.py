"""
Number of subarrays with k number of odd elements
"""

arr=[4, 3, 2, 3, 4]
for i in range(len(arr)):
    arr[i]=arr[i]&1
curr=0
ans=0
k=2
d={}
for i in arr:
    curr+=i
    if curr==k:
        ans+=1
    if curr-k in d:
        ans+=d[curr-k]
    if curr in d:
        d[curr]+=1
    else:
        d[curr]=1
print(ans)