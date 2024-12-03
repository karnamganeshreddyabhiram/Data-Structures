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
            print(t.data)
            t=t.next
    def isPalindrome(self):
        sta = []
        t=self.head
        t1=self.head
        while(t):
            sta.append(t.data)
            t=t.next
        ans = False
        t=self.head
        while(t1 and t1.next):
            s=sta.pop()
            if t.data==s:
                ans=True
            else:
                return False
            t=t.next
            t1=t1.next.next
        return ans

l = LinkedList()
l.pushEnd(10)
l.pushEnd(20)
l.pushEnd(10)
l.printList()
l.isPalindrome()