class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if(root==None):
        return Node(data)
    if(root.data<data):
        root.right=insert(root.right, data)
    elif(root.data>data):
        root.left=insert(root.left, data)
    return root

def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
def findMin(root):
    while(root.left):
        root=root.left
    return root

def deleteNode(root,data):
    if(root==None):
        return
    if(data>root.data):
        root.right=deleteNode(root.right, data)
    elif(data<root.data):
        root.left=deleteNode(root.left, data)
    else:
        if(root.right==None):
            tmp=root.left
            root=None
            return tmp
        elif(root.left==None):
            tmp=root.right
            root=None
            return tmp
        else:
            tmp=findMin(root.right)
            root.data=tmp.data
            root.right=deleteNode(root.right, tmp.key)
    return root
            

root=None
root=insert(root, 30)
root=insert(root, 10)
root=insert(root, 40)
root=insert(root, 100)
inorder(root)
root=deleteNode(root, 40)
inorder(root)