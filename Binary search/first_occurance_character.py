def bs(n,k):
    l=0
    r=n-1
    ans=-1
    while(l<=r):
        mid=(l+r)//2
        if(A[mid]==k):
            ans=mid
            r=mid-1
        elif(A[mid]>k):
            r=mid-1
        else:
            l=mid+1
    return ans

A=[1,2,3,3,4]
k=3
print(bs(len(A),k))