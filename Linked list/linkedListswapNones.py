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
    def swapNodes(self,x,y):
        if x==y:
            return
        px=self.head
        prevx=None
        while(px and px.data!=x):
            prevx=px
            px=px.next
        py=self.head
        prevy=None
        while(py and py.data!=y):
            prevy=py
            py=py.next
        if px==None or py==None:
            return
        if prevx!=None:
            prevx.next=py
        else:
            self.head=py
        if prevy!=None:
            prevy.next=px
        else:
            self.head=px
        t=px.next
        px.next=py.next
        py.next=t

l = LinkedList()
l.pushEnd(10)
l.pushEnd(20)
l.pushEnd(30)
l.pushEnd(40)
l.swapNodes(10, 30)
l.printList()
