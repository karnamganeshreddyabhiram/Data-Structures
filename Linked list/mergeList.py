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

def mergeLists(l1,l2):
    t1=l1.head
    t2=l2.head
    res = LinkedList()
    while(t1 and t2):
        if(t1.data<t2.data):
            res.pushEnd(t1.data)
            t1=t1.next
        else:
            res.pushEnd(t2.data)
            t2=t2.next
    if(t1!=None):
        while(t1):
            res.pushEnd(t1.data)
            t1=t1.next
    if(t2!=None):
        while(t2):
            res.pushEnd(t2.data)
            t2=t2.next
    res.printList()

    
l = LinkedList()
l.pushEnd(1)
l.pushEnd(2)
l.pushEnd(8)
l.pushEnd(10)

l1 = LinkedList()
l1.pushEnd(3)
l1.pushEnd(4)
l1.pushEnd(12)
l1.pushEnd(21)

mergeLists(l, l1)