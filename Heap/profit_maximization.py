#https://www.interviewbit.com/problems/profit-maximisation/
import heapq
A=[2,3]
B=3
heap=[]
heapq.heapify(heap)
for i in A:
    heapq.heappush(heap,i*-1)
ans=0
for i in range(B):
    t=(heapq.heappop(heap)*-1)
    ans+=t
    heapq.heappush(heap,-1*(t-1))
print(ans)