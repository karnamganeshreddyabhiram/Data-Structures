class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
    def pushEnd(self,data):
        n=Node(data)
        if(self.end==None):
            self.head=n
            self.end=n
        self.end.next=n
        self.end=n
    def printList(self):
        t=self.head
        while(t):
            print(t.data, end=" ")
            t=t.next

def findIntersection(l1,l2):
    h=set()
    t=l1.head
    while(t):
        h.add(t)
        t=t.next
    t=l2.head
    while(t):
        if t in h:
            return True
        t=t.next
    return False

l1=LinkedList()
l1.pushEnd(1)
l1.pushEnd(2)
l1.pushEnd(3)
l1.pushEnd(4)

l2=LinkedList()
l2.pushEnd(1)
l2.pushEnd(2)
l2.pushEnd(3)
l2.pushEnd(4)
l2.end.next=l1.head

findIntersection(l1, l2)
