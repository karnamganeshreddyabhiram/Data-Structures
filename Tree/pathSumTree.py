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

def paths(root,pathSum):
    if root==None:
        return
    else:
        if root.left==None and root.right==None:
            pathSum+=root.data
            print(pathSum)
        pathSum+=root.data
        paths(root.left,pathSum)
        paths(root.right,pathSum)
        pathSum-=root.data
        
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
print(paths(r,0))
