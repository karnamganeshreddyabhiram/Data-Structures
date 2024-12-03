n=8
e=[[0,1],[1,2],[2,6],[0,3],[3,4],[1,3],[4,5],[5,6],[6,7],[7,8],[6,8]]
g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
q=[]
v=[float('inf') for i in range(n+1)]
q=[0]
v[0]=0
while(q):
    c=q.pop(0)
    for i in g[c]:
        if(v[c]+1<v[i]):
            v[i]=v[c]+1
            q.append(i)
print(v)
            