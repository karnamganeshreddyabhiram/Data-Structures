import heapq
l=[[3, 5, 7],[0, 6],[0, 6, 28]]
heap=[]
heapq.heapify(heap)
for i in range(len(l)):
    if l[i]:
        heapq.heappush(heap, (l[i][0],i,0))
ans=[]
while heap:
    num,r,c=heapq.heappop(heap)
    ans.append(num)
    if(c<len(l[r])-1):
        heapq.heappush(heap,(l[r][c+1],r,c+1))
print(ans)        
