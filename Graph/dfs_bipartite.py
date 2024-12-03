def dfs(node):
    if(color[node]==-1):
        color[node]=1
    for i in g[node]:
        if(color[i]==-1):
            color[i]=1-color[node]
            if(not dfs(i)):
                return False
        elif(color[i]==color[node]):
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
        if(not dfs(i)):
            print("No, it is not a bi partite graph")
            break