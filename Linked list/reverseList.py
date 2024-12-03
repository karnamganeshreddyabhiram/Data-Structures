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
    def reverseList(self):
        curr=self.head
        self.end=curr
        prev=None
        next=None
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

l = LinkedList()
l.pushEnd(1)
l.pushEnd(2)
l.pushEnd(3)
l.pushEnd(4)
l.reverseList()
l.printList()   