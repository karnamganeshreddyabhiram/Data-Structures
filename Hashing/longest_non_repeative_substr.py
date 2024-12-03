"""
Longest substring without repeating characters
"""

s="abaabcda"
d={}
maxi=0
l=0
r=0
n=len(s)
while r<n:
    if(s[r] in d):
        l=max(l,d[s[r]]+1)
    d[s[r]]=r
    maxi=max(maxi,r-l+1)
    r+=1
print(maxi)
