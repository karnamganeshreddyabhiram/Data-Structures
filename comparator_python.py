from functools import cmp_to_key
def comparator(a,b):
    if(a[1]>b[1]):
        return 1
    elif(a[1]<b[1]):
        return -1
    else:
        return 0
arr=[[1,4],[2,3],[3,1]]
arr=sorted(arr,key=cmp_to_key(comparator))
print(arr)    
