"""
Number of subarrays with given sum
"""

d={}
arr=[10, 2, -2, -20, 10] 
s=-10
curr=0
ans=0
for i in arr:
    curr+=i
    if curr==s:
        ans+=1
    if curr-s in d:
        ans+=d[curr-s]
    if curr not in d:
        d[curr]=1
    else:
        d[curr]+=1
print(ans)
    