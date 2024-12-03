"""
Find the length of longest subarray sum which equals to 0
"""

arr=[1,3,3,-1,-3,-3,4,-4]
d={}
s=0
maxi=0
for i in range(len(arr)):
    s+=arr[i]
    if s==0:
        maxi=i+1
    else:
        if s in d:
            maxi=max(maxi,(i-d[s]))
        else:
            d[s]=i
print(maxi)