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

def height(root,maxi):
    if root==None:
        return 0
    lh = height(root.left,maxi)
    rh = height(root.right,maxi)
    maxi[0]=max(maxi[0],lh+rh)
    return 1+max(lh,rh)

r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
maxi=[0]
height(r,maxi)
print(maxi[0])
