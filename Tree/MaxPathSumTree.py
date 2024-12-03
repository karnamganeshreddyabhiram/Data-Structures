from TreeBase import Node, insert 

def MaxPathSum(root,maxi):
    if root==None:
        return 0
    ls = MaxPathSum(root.left, maxi)
    rs = MaxPathSum(root.right, maxi)
    maxi[0]=max(maxi[0],ls+rs+root.data)
    return max(ls,rs)+root.data
    
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
maxi=[0]
MaxPathSum(r, maxi)
print(maxi[0])