class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.end=None
    def push(self,data):
        n = Node(data)
        n.next=self.head
        self.head=n
    def pushEnd(self,data):
        n = Node(data)
        if(self.end==None):
            self.head=n
            self.end=n
        self.end.next = n
        self.end = n
    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

l = LinkedList()
l.pushEnd(10)
l.pushEnd(20)
l.pushEnd(30)
l.pushEnd(40)
l.printList()

l1 = LinkedList()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(40)
l1.printList()