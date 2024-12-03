def fact(n):
    if(n==1):
        return 1
    return n*(fact(n-1))
print(fact(8))

def reverse(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    reverse(arr,l+1,r-1)
arr=[1,2,3,4]
reverse(arr,0,3)
print(arr)

def reverseAlt(arr,i,n):
    if i>=n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    reverseAlt(arr,i+1,n)
arr=[1,2,3,4]
reverseAlt(arr,0,4)
print(arr)