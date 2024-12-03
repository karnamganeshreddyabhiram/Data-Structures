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
    def detectLoop(self):
        slow=self.head
        fast=self.head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
    
l = LinkedList()
l.pushEnd(10)
l.pushEnd(10)
l.pushEnd(10)
l.detectLoop()