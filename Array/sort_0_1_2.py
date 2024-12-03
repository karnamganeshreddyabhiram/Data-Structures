"""
Sort 0s, 1s, 2s
Dutch national flag algorithm
We have 3 pointers low, mid, high. Low and mid initialized to 0 and high to end of the array
0 to mid all 0s
mid to high all 1s
high to end all 2s
Swap accordingly
"""

arr=[0,0,1,1,0,2,1,2,0]
low=0
mid=0
high=len(arr)-1

while(mid<=high):
    if(arr[mid]==0):
        arr[low],arr[mid]=arr[mid],arr[low]
        low+=1
        mid+=1
    elif(arr[mid]==1):
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
print(arr)
    
        