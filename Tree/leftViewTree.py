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

def leftView(root,level,d):
    if root==None:
        return
    if len(d)==level:
        d.append(root.data)
    leftView(root.left,level+1,d)
    leftView(root.right,level+1,d)

def rightView(root,level,d):
    if root==None:
        return
    if len(d)==level:
        d.append(root.data)
    leftView(root.right,level+1,d)
    leftView(root.left,level+1,d)

r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
d=[]
leftView(r, 0, d)
print(d)
d=[]
rightView(r, 0, d)
print(d)