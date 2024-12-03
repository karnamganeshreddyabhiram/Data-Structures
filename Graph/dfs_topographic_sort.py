def dfs(n):
    v[n]=True
    for i in g[n]:
        if v[i]==False:
            dfs(i)
    sta.append(n)
n=5
e=[[4,0],[4,1],[3,1],[2,3],[5,2],[5,0]]

g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])

v=[False for i in range(n+1)]
sta=[]
for i in range(n+1):
    if v[i]==False:
        dfs(i)
print(sta[::-1])
