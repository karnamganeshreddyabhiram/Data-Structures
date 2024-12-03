class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.end=None
        self.n=0
    def insert(self,data):
        n=Node(data)
        self.n+=1
        if(self.head==None):
            self.head=n
            self.end=n
            return
        self.end.next=n
        self.end=n
    def print_list(self):
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next
    def delete_from_last(self,k):
        k=self.n-k
        t=self.head
        c=0
        if(k==0):
            self.head=self.head.next
            return
        while(c!=k):
            prev=t
            t=t.next
            c+=1
        prev.next=t.next
        
l=LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.print_list()  
print("")
l.delete_from_last(2)
l.print_list()