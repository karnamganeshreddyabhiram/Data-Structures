def dfs(node,par,time):
    v[node]=1
    t0[node]=lt[node]=time
    time+=1
    for it in g[node]:
        if(it==par):
            continue
        if(v[it]==0):
            dfs(it,node,time)
            lt[node]=min(lt[node],lt[it])
            if(lt[it]>t0[node]):
                print(it,node)
        else:
            lt[node]=min(lt[node],t0[it])
       
e=[[0,1],[1,2],[0,2],[2,3],[3,4],[4,5],[3,5]]
n=6
g=[[] for i in range(n)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
v=[0]*n
t0=[0]*n
lt=[0]*n
dfs(0,-1,0)