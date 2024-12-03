import heapq #Maintains min heap
li=[5,7,9,1,3]
#Making the list into a heap
heapq.heapify(li)
print(li)

#Pushing an element into heap
heapq.heappush(li, 4)
print(li)

#To popout the smallest element
print(heapq.heappop(li))


#To maintain max heap, insert negative values in it by multiplying with -1
li=[5,7,9,1,3]
heap=[]
heapq.heapify(heap)
for i in li:
    heapq.heappush(heap, -1*i)
for i in heap:
    print(-1*i,end=" ")
print("")
print(heapq.heappop(heap)*-1)