"""
Find duplicate number
From an array of 1 to n
"""
arr=[1,2,3,4,4,5,6,7,8]
n=len(arr)
slow=arr[0]
fast=arr[arr[0]]
while(slow!=fast):
    slow=arr[slow]
    fast=arr[arr[fast]]
fast=arr[0]
while(slow!=fast):
    slow=arr[slow]
    fast=arr[arr[fast]]
print(slow)