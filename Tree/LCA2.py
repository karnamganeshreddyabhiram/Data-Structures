from TreeBase import insert 
def LCA(root,n1,n2):
    if(root==None or root.data==n1 or root.data==n2):
        return root
    l=LCA(root.left,n1,n2)
    r=LCA(root.right,n1,n2)
    #While Comming out of children nodes
    if(l==None):
        return r
    elif(r==None):
        return l
    else:
        return root
    
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
print(LCA(r,10,50).data)