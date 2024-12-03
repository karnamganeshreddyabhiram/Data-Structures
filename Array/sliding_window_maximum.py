from collections import deque
dq=deque()
arr=[1,3,-1,-3,5,3,6,7]
ans=[]
k=3
for i in range(len(arr)):
    if(len(dq) and dq[0]==i-k):
        dq.popleft()
    while(len(dq) and arr[i]>arr[dq[-1]]):
        dq.pop()
    dq.append(i)
    if(i>=k-1):
        ans.append(arr[dq[0]])
print(ans)
    
    