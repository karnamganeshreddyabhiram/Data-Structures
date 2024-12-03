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
    def removeFromEnd(self,n):
        c=0
        t=self.head
        while(t):
            t=t.next
            c+=1
        n=c-n
        c=0
        prev=None
        t=self.head
        while(t and c<n):
            prev=t
            t=t.next
            c+=1
        prev.next=t.next

l = LinkedList()
l.pushEnd(1)
l.pushEnd(2)
l.pushEnd(3)
l.pushEnd(4)
l.removeFromEnd(2)
l.printList()
