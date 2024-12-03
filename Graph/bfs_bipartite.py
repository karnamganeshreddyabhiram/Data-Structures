def isBiPartite(n):
    q=[]
    q.append(n)
    color[n]=1
    while(q):
        c=q.pop(0)
        for i in g[c]:
            if color[i]==-1:
                q.append(i)
                color[i]=1-color[c]
            elif color[c]==color[i]:
                return False
    return True

n=8
e=[[1,2],[2,3],[3,4],[4,5],[2,8],[8,5],[5,6],[6,7]]
g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
color=[-1 for i in range(n+1)]
for i in range(1,n+1):
    if(color[i]==-1):
        if(not isBiPartite(i)):
            print("No, it is not a bi partite graph")