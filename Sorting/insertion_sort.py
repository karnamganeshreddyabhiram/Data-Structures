arr = [3,4,1,2]
n=len(arr)
for i in range(2,n):
    key = arr[i]
    j=i-1
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)