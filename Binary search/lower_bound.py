"""
Lower bound -> The next greater element for a given number
"""

def bs(n,k):
    l=0
    r=n-1
    ans=n
    while(l<=r):
        mid=(l+r)//2
        if(A[mid]>=k):
            r=mid-1
            ans=A[mid]
        else:
            l=mid+1
    return ans

A=[1,2,3,4,5,10,12,17]
print(bs(len(A),13))
    