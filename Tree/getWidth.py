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

def inorder(root):
    if root:
        inorder(root.right)
        print(root.data)
        inorder(root.left)

def getWidth(root):
    q=[root]
    maxi=len(q)
    while(q):
        c=len(q)
        maxi=max(maxi,len(q))
        for i in range(c):
            r=q.pop(0)
            if(r.left):
                q.append(r.left)
            if(r.right):
                q.append(r.right)
    return maxi

r = Node(40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
print(getWidth(r))