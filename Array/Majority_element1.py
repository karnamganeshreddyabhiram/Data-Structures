"""
Majority element
Find the element which repeats more than [n/2] times
Moores voting algorithm
"""

a=[1,3,3]
c=0
ele=-1
for i in range(len(a)):
    if c==0:
        ele=a[i]
    if ele==a[i]:
        c+=1
    else:
        c-=1
print(ele)