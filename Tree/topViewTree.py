from TreeBase import Node, insert 
def topView(root):
    q=[[root,0,0]]
    d=[]
    lv=[]
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
d=topView(r)

vo={}
for i in d:
    if i[1] not in vo:
        vo[i[1]]=[[i[0],i[2]]]
    else:
        vo[i[1]].append([i[0],i[2]])

for i in vo:
    vo[i]=sorted(vo[i], key=lambda x: x[1])

for i in vo:
    print(vo[i][0][0])