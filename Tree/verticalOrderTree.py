from TreeBase import Node, insert 
def verticalOrder(root):
    q=[[root,0,0]]
    d=[]
    while(q):
        c=q.pop(0)
        d.append([c[0].data,c[1],c[2]])
        if(c[0].left):
            q.append([c[0].left,c[1]-1,c[2]+1])
        if(c[0].right):
            q.append([c[0].right,c[1]+1,c[2]+1])
    return d
    
    
r=None
r = insert(r,40)
r = insert(r,30)
r = insert(r,50)
r = insert(r,10)
r = insert(r,20)
d=verticalOrder(r)
v={}
for i in d:
    if i[1] in v:
        v[i[1]].append(i[0])
    else:
        v[i[1]]=[i[0]]
print(v)