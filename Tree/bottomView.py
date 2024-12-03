from TreeBase import Node, insert 
def bottomView(root):
    q=[[root,0]]
    d={}
    while(q):
        c=q.pop(0)
        if c[1] in d:
            d[c[1]].append(c[0].data)
        else:
            d[c[1]]=[c[0].data]
        if c[0].left:
            q.append([c[0].left,c[1]-1])
        if c[0].right:
            q.append([c[0].right,c[1]+1])
    return d
        
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
d=bottomView(r)
v=[]
for i in d:
    v.append(d[i][-1])
print(v)