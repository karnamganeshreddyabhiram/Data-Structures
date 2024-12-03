"""
Find the triplet which gives the maximum sum such that a[i]<=a[j]<=a[k] and i<=j<=j
"""

a=[2,4,3,1,5,9]
r=[0]*len(a)
maxi=a[len(a)-1]
for i in range(len(a)-1,-1,-1):
    maxi=max(maxi,a[i])
    r[i]=maxi
s=set()
ans=float('-inf')
for i in range(len(a)-1):
    s.add(a[i])
    l=list(s)
    ans=max(a[i]+l[l.index(a[i])-1]+r[i],ans)
print(ans)