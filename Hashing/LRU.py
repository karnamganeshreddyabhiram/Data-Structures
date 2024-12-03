class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.d={}
        self.n=0
    def insert(self,data):
        n=Node(data)
        n.next=self.head.next
        self.head.next.prev=n
        self.head.next=n
        n.prev=self.head
    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def printList(self):
        t=self.tail
        while(t):
            print(t.data)
            t=t.prev
    def put(self,key,value):
        if(key in self.d):
            v=self.d[key]
            del self.d[key]
            self.delete(v)
        elif(self.n==3):
            self.delete(self.tail.prev)
            del self.d[self.tail.prev.data]
        self.insert(value)
        self.d[key]=self.head.next
        self.n+=1
            
    def get(self,key):
        if key in self.d:
            v=self.d[key]
            ans=v.data
            self.delete(v)
            self.insert(ans)
            self.d[key]=self.head.next
            return ans
        return -1

l=LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.put(1,10)
l.put(2,20)
l.put(3,30)
print(l.get(1))
print(l.get(2))
print(l.get(3))
print(l.get(1))
l.put(3,30)
print(l.get(3))
    
        
