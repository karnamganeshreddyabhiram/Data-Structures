class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(root,data):
    if(root==None):
        return Node(data)
    else:
        if(root.data>data):
            root.left = insert(root.left,data)
        else:
            root.right = insert(root.right,data)
    return root

def inorder(root):
    if(root==None):
        return
    if(root.left==None and root.right==None):
        ans.append(root.data)
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def isLeaf(r):
    if(r.left or r.right):
        return False
    return True

def leftSide(r):
    while(r):
        if(not isLeaf(r)):
            ans.append(r.data)
        if(r.left):
            r=r.left
        else:
            r=r.right

def rightSide(r):
    while(r):
        if(not isLeaf((r))):
            ans.append(r)
        if(r.right):
            r=r.right
        else:
            r=r.left
r=Node(40)
r=insert(r,30)
r=insert(r,10)
r=insert(r,20)
r=insert(r,50)
ans=[]
leftSide(r)
inorder(r)
rightSide(r.right)
print(ans)