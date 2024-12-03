"""
Find the frequency of an array element
First occurance-last occurance+1
"""

def findFreq(k):
    l=0
    r=len(arr)-1
    ans1=0
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]==k):
            r=mid-1
            ans1=mid
        elif(arr[mid]>k):
            r=mid-1
        else:
            l=mid+1
    ans2=0
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]==k):
            l=mid+1
            ans2=mid
        elif(arr[mid]>k):
            r=mid-1
        else:
            l=mid+1
    return ans2-ans1+1
    
    
arr=[1,1,2,3,4,4,4,4]
print(findFreq(4))
