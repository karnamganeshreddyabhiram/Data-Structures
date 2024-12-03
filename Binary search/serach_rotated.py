"""
Search on rotated sorted array
At ay point of time, either life or right or both parts of the arrays are sorted
In the sorted array check wheather the required element is there or not
"""

def find(k):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]==k):
            return mid
        #if left part is sorted
        if(arr[l]<=arr[mid]):
            if(k>=arr[l] and k<=arr[mid]):
                r=mid-1
            else:
                l=mid+1
        #if right part is sorted
        else:
            if(k>=arr[mid] and k<=arr[r]):
                l=mid+1
            else:
                r=mid-1
    return -1

arr=[7,8,9,1,2,3,4,5,6]
print(find(3))