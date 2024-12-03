def minDist():
    mini = float("inf")
    idx=0
    for i in range(len(v)):
        if(mini>d[i] and v[i]==False):
            mini=d[i]
            idx=i
    return idx

def dijkstra(src):
    d[src]= 0
    for i in range(len(v)):
        x=minDist()
        v[x]= True
        for j in range(len(v)):
            if g[i][j]>0 and g[i][j]+d[x]<d[j] and v[j]==False:
                d[j]=d[x]+g[i][j]
            

g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

n=len(g)
v= [False for i in range(n)]
d= [float("inf") for i in range(n)]
dijkstra(0)
print(d)