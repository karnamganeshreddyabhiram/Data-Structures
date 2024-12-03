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

def height(root):
    if root==None:
        return 0
    lh = 1+height(root.left)
    rh = 1+height(root.right)
    return max(lh,rh)

def diameter(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh+rh,diameter(root.left),diameter(root.right))
    

r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
print(diameter(r))
