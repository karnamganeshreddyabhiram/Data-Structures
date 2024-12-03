def heapify(arr,n,i):
    l=2*i+1
    r=2*i+2
    largest=i
    if(l<n and arr[l]>arr[i]):
        largest=l
    if(r<n and arr[r]>arr[largest]):
        largest=r
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr, n,largest)

def heapSort(arr,n):
    s=n//2-1
    for i in range(s,-1,-1):
        heapify(arr,n, i)
    for i in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i-1,0)

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heapSort(arr,len(arr))
print(arr)