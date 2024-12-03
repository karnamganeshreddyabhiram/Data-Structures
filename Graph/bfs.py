n=7
e=[[1,2],[2,3],[2,7],[7,5],[3,5],[4,6]]
g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
bfs=[]
v=[False for i in range(n+1)]
for i in range(1,n+1):
    if v[i]==False:
        q=[i]
        v[i]=True
        while(q):
            c=q.pop(0)
            bfs.append(c)
            for j in g[c]:
                if(v[j]==False):
                    v[j]=True    
                    q.append(j)
print(bfs)
            
            