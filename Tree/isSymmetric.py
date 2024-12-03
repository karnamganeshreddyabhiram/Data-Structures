class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isSymmetric(left,right):
    if(left==None or right==None):
        return (left==right)
    if(left.data!=right.data):
        return False
    l=isSymmetric(left.left, right.right)
    r=isSymmetric(left.right, right.left)
    return l and r

r=Node(10)
r.left=Node(20)
r.right=Node(20)
r.left.right=Node(30)
r.right.left=Node(30)
print(isSymmetric(r.left, r.right))