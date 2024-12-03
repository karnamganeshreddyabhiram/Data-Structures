def f(i,v,dfs):
    dfs.append(i)
    v[i] = True
    for n in g[i]:
        if v[n]==False:
            f(n,v,dfs)

n=7
e=[[1,2],[2,3],[2,7],[7,5],[3,5],[4,6]]
g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
v=[False for i in range(n+1)]
dfs = []
for i in range(1,n+1):
    if(v[i]==False):
        f(i,v,dfs)
print(dfs)