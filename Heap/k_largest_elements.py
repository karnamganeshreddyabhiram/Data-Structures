import heapq
A=[3,10,2,1]
B=2
heap=[]
heapq.heapify(heap)
for i in A:
    heapq.heappush(heap,-1*i)
ans=[]
for i in range(B):
    ans.append(heapq.heappop(heap)*-1)
print(ans)
