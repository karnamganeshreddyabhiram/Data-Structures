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
    if root==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def printAllPaths(root,path):
    if root==None:
        return
    path.append(root.data)
    if root.left==None and root.right==None:
        print(path)
    printAllPaths(root.left, path)
    printAllPaths(root.right, path)
    path.pop()

root=None
root=insert(root, 40)
root=insert(root, 30)
root=insert(root, 10)
root=insert(root, 20)
root=insert(root, 50)
inorder(root)
printAllPaths(root, [])
