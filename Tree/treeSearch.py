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
            root.right=insert(root.right, data)
        else:
            root.left=insert(root.left, data)
        return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def search(root,key):
    if root:
        if root.data==key:
            return root
        elif root.data<key:
            return search(root.right, key)
        else:
            return search(root.left, key)
            
root=None
root=insert(root, 40)
root=insert(root, 30)
root=insert(root, 10)
root=insert(root, 20)
root=insert(root, 50)
inorder(root)
if search(root,30):
    print("Found")
else:
    print("Not found")