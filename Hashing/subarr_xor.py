"""
Number of subarrays whose XoR gives the target value
https://www.youtube.com/watch?v=lO9R5CaGRPY&list=PLgUwDviBIf0rVwua0kKYlsS_ik_1lyVK_&index=5
"""

arr=[4,2,2,6,4]
d={}
c=0
xor=0
k=6
for i in arr:
    xor^=i
    if xor in d:
        d[xor]+=1
    else:
        d[xor]=1
    if xor^k in d:
        c+=d[xor^k]
    if xor==k:
        c+=1
print(c)