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

def findLCA(d1,d2):
    i=0
    n1=len(d1)
    n2=len(d2)
    while(i<n1 and i<n2):
        if d1[i]!=d2[i]:
            break
        i+=1
    if i==0:
        return d1[0]
    else:
        return d1[i-1]
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
ds=[]
findPath(r, 50,ds)
d1=ds.copy()
ds=[]
findPath(r, 10,ds)
d2=ds.copy()
print(findLCA(d1,d2))