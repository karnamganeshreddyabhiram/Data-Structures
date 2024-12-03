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

def getPath(root,data):
    if(root==None):
        return False
    ds.append(root.data)
    if(root.data==data):
        return True
    if(getPath(root.left, data) or getPath(root.right, data)):
        return True
    ds.pop()
    return False

r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
ds=[]
if(getPath(r, 10)):
    print(ds)
    