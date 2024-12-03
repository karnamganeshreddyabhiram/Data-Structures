def bs(l,r,k):
    if(l>r):
        return -1
    mid=(l+r)//2
    if(A[mid]>k):
        return bs(l,mid-1)
    elif(A[mid]>k):
        return bs(mid+1,r)
    else:
        return mid

A=[1,2,3,4]
bs(0,len(A),3)