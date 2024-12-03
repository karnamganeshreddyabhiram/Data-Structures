"""
Find missing and repeating number from 1 to n
"""
arr=[1,2,2,3,4,5,7,8]
n=len(arr)
x=n*(n+1)//2
y=sum(arr)
z=(x-y)
x2=n*(n+1)*(2*n+1)//6
y2=0
for i in arr:
    y2+=(i**2)
z2=x2-y2
z1=z2//z
r1=(z+z1)//2
r2=(z-z1)//2
print(r1,abs(r2))