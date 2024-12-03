"""
Find maximum rectangle are in a histogram
The idea is to find number of consecutive elements on left and right which are greater than
or equal to arr[i] (r-l+1)*arr[i]
(right smaller index - left smaller index)*arr[i]
Pre requisite -> Next greater element
"""

arr = [2,1,5,6,2,3,1]
n=len(arr)
s=[]
nl=[0]*n
i=0
while(i<n):
    while(len(s)>0 and arr[s[-1]]>=arr[i]):
        s.pop()
    if len(s)==0:
        nl[i]=0
    else:
        nl[i]=s[-1]+1
    s.append(i)
    i+=1
print(nl)

s=[]
nr=[0]*n
i=n-1
while(i>=0):
    while(len(s)>0 and arr[s[-1]]>=arr[i]):
        s.pop()
    if len(s)==0:
        nr[i]=n-1
    else:
        nr[i]=s[-1]-1
    s.append(i)
    i-=1
print(nr)

maxi=0
for i in range(n):
    maxi=max(maxi,(nr[i]-nl[i]+1)*arr[i])
print(maxi)