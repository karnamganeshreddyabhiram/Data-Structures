class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isSymmetricHelp(left,right):
    if left==None or right==None:
        return left==right
    if left.data!=right.data:
        return False
    return isSymmetricHelp(left.left, right.right) and isSymmetricHelp(left.right, right.left)

def isSymmetric(root):
    if root==None or isSymmetricHelp(root.left,root.right):
        return True
    return False

r=Node(10)
r.left=Node(20)
r.right=Node(20)
r.left.right=Node(30)
r.right.left=Node(30)
print(isSymmetric(r))