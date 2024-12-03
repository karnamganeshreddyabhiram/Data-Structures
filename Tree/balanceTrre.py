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

def balancedTree(root):
    if root==None:
        return 0
    l=balancedTree(root.left)
    if(l==-1):
        return -1
    r=balancedTree(root.right)
    if(r==-1):
        return -1
    if(abs(l-r)>1):
        return -1
    return 1+max(l,r)

r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
print(balancedTree(r))