def dfs(node,par,timer):
    tin[node]=low[node]=timer
    timer+=1
    v[node]=True
    for i in g[node]:
        if i==par:
            continue
        if v[i]==False:
            dfs(i,node,timer)
            low[node]=min(low[node],low[i])
            if(low[i]>tin[node]):
                print(i,node)
        else:
            low[node]=min(low[node],tin[i])

n=4
e=[[0,1],[0,2],[1,2],[1,3],[3,4]]
g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])

v = [False for i in range(n+1)]
tin = [0 for i in range(n+1)]
low = [0 for i in range(n+1)]
for i in range(n+1):
    if v[i]==False:
        dfs(i,-1,0)