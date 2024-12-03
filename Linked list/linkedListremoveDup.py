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
    def removeDup(self):
        t = self.head
        while(t):
            prev = t
            while(prev and prev.next and prev.data == prev.next.data):
                prev=prev.next
            t.next=prev.next
            t=prev.next
    def removeDupUnSort(self):
        h=set()
        t=self.head
        h.add(t.data)
        while(t.next):
            if t.next.data in h:
                t.next=t.next.next
            else:
                h.add(t.next.data)
                t=t.next
            

l = LinkedList()
l.pushEnd(10)
l.pushEnd(10)
l.pushEnd(10)
l.pushEnd(20)
l.pushEnd(30)
l.pushEnd(40)
l.pushEnd(40)
l.removeDup()
l.printList()

l1 = LinkedList()
l1.pushEnd(10)
l1.pushEnd(20)
l1.pushEnd(10)
l1.pushEnd(30)
l1.pushEnd(30)
l1.pushEnd(10)
l1.pushEnd(40)
l1.removeDupUnSort()
l1.printList()
