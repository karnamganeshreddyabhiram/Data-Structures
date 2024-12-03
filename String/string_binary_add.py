A="101"
B="11111"
i=len(A)-1
j=len(B)-1
s=0
ans=""
while(i>=0 or j>=0 or s==1):
    if i>=0:
        s+=int(A[i])
    if j>=0:
        s+=int(B[j])
    ans=str(s%2)+ans
    s=s//2
    i-=1
    j-=1
print(ans)