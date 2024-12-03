class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    def removeDup(self):
        t=self.head
        while(t):
            prev=t
            while(t.next and t.next.data==t.data):
                t=t.next
            prev.next=t.next
            t=t.next
    def removeDup2(self):
        self.push(0)
        t=self.head.next
        prev=self.head
        while(t):
            while(t.next and t.next.data==t.data):
                t=t.next
            if(prev.next==t):
                prev=prev.next
            else:
                prev.next=t.next
            t=t.next
        self.head=self.head.next
    def print_list(self):
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next

l=LinkedList()
l.push(4)
l.push(3)
l.push(2)
l.push(2)
l.push(1)
l.push(1)
l.push(1)            
l.removeDup2()
l.print_list()