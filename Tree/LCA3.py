from TreeBase import insert

def findPath(root,k):
    if(root==None):
        return
    if(root.data==k):
        ds.append(root.data)
        print(ds)
    ds.append(root.data)
    findPath(root.left,k)
    findPath(root.right,k)
    ds.pop()
    
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
findPath(r, 50)
d1=ds.copy()
ds=[]
findPath(r, 10)
d2=ds.copy()
print(findLCA(d1,d2))