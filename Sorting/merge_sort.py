def merge(arr, l, m, r):
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    i = 0    
    j = 0    
    k = l    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
 
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
arr=[3,4,1,2]
mergeSort(arr, 0, len(arr)-1)
print(arr)