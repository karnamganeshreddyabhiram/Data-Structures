def checkCycle(n,npar):
    v[n]=True
    for i in g[n]:
        if v[i]==False:
            if(checkCycle(i, n)):
                return True
        elif npar!=i:
            return True
    return False

n=11
e=[[1,2],[2,4],[3,5],[5,6],[6,7],[7,8],[5,10],[10,9],[9,8],[8,11]]

g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
bfs=[]
v=[False for i in range(n+1)]
for i in range(1,n+1):
    if v[i]==False:
        if(checkCycle(i,-1)):
            print("Yes cycle is there")
            break