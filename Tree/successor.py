from TreeBase import insert 
def successor(root,data):
    if(root==None):
        return
    if(data>=root.data):
        successor(root.right, data)
    else:
        succ[0]=root.data
        successor(root.left, data)

r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
succ=[None]
successor(r, 30)
print(succ[0])