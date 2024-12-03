"""
Next perumutation
1) Start from last index and find at which index we get a[i]<a[i+1]
2) Again start from last index and find where we get an element which is greater than a[i]
3) Swap a[i] and that number
4) Reverse the array from a[i] 
"""

a=[1,3,5,4,2]
i=len(a)-2
while(i>=0 and a[i]>=a[i+1]):
    i-=1
if i>=0:
    j=len(a)-2
    while(j>=0 and a[j]<=a[i]):
        j-=1
    a[i],a[j]=a[j],a[i]
    i+=1
j=len(a)-1
while(i<j):
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
print(a)