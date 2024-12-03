class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder(root):
    if(root==None):
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def reorder(root):
    if(root==None):
        return
    c=0
    if(root.left):
        c+=root.left.data
    if(root.right):
        c+=root.right.data
    if(c>=root.data):
        root.data=c
    else:
        if(root.left):
            root.left.data=root.data
        if(root.right):
            root.right.data=root.data
    reorder(root.left)
    reorder(root.right)
    t=0
    if(root.left):
        t+=root.left.data
    if(root.right):
        t+=root.right.data
    if(root.left or root.right):
        root.data=t
        
root=Node(2)
root.left=Node(35)
root.right=Node(10)
root.left.left=Node(2)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(2)
preorder(root)
print("")
reorder(root)
preorder(root)