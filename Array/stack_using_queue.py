class Stack:
    def __init__(self):
        self.q=[]
        self.n=0
    def pop(self):
        if(self.n==0):
            return "Queue is empty"
        r=self.q.pop()
        self.n-=1
        return r
    def push(self,data):
        self.q.append(data)
        self.n+=1
        c=self.n-1
        while(c):
            self.q.append(self.q.pop())
            c-=1
    def top(self):
        return self.q[self.n-1]

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
s.push(40) 
print(s.top())
print(s.pop())       