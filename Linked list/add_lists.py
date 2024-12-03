class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
     def __init__(self):
         self.head=None
     def insert(self,data):
         n = Node(data)
         n.next=self.head
         self.head=n
    
     def print_list(self):
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next

def add_lists(l,l1):
    t=LinkedList()
    c=0
    a1=l.head
    a2=l1.head
    while(a1 or a2 or c):
        s=0
        if a1:
            s+=a1.data
            a1=a1.next
        if a2:
            s+=a2.data
            a2=a2.next
        s+=c
        c=s//10
        s=s%10
        t.insert(s)
    t.print_list()
        
l=LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)

l1=LinkedList()
l1.insert(9)
l1.insert(9)
l1.insert(9)

add_lists(l, l1)