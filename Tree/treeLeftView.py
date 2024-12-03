class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(root,data):
    if root==None:
        return Node(data)
    else:
        if root.data==data:
            return root
        elif root.data<data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
    return root

def levelOrder(root):
    q=[root]
    a=[]
    while(q):
        t=[]
        n=len(q)
        while(n):
            curr=q.pop(0)
            t.append(curr.data)
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
            n-=1
        a.append(t)
    return a
        
r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
a=levelOrder(r)
for i in a:
    print(i[0])