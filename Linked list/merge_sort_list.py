class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        if(self.head==None):
            self.head=Node(data)
            return
        n=Node(data)
        n.next=self.head
        self.head=n
    def print_list(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next

def find_middle(head):
    s=head
    f=head
    while(f.next and f.next.next):
        f=f.next.next
        s=s.next
    return s

def merge(l,r):
    d=Node(-1)
    td=d
    while(l and r):
        if(l.data<r.data):
            d.next=l
            l=l.next
            d=d.next
        else:
            d.next=r
            r=r.next
            d=d.next
    while(l):
        d.next=l
        l=l.next
        d=d.next
    while(r):
        d.next=r
        r=r.next
        d=d.next
    return td.next

def merge_sort(head):
    if(head.next==None):
        return head
    mid=find_middle(head)
    tail=mid.next
    mid.next=None
    l = merge_sort(head)
    r = merge_sort(tail)
    return merge(l,r)

l=LinkedList()
l.append(3)
l.append(2)
l.append(4)
l.append(1)
l1=merge_sort(l.head)
while(l1):
    print(l1.data)
    l1=l1.next