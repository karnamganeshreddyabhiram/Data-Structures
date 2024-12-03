from TreeBase import Node, insert 
def findPath(root,x,ds):
    if(root==None):
        return False
    if(root.data==x):
        ds.append(x)
        return True
    ds.append(root.data)
    if(findPath(root.left, x, ds)):
        return True
    if(findPath(root.right, x, ds)):
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
findPath(r, 50,ds)
print(ds)
ds=[]
findPath(r, 10,ds)
print(ds)
