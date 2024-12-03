def checkCycle(n,npar):
    v[n]=True
    dfsv[n]=True
    for i in g[n]:
        if v[i]==False:
            if(checkCycle(i, n)):
                return True
        elif dfsv[n]:
            return True
    dfsv[n]=False
    return False

n=9
e=[[1,2],[2,3],[3,4],[4,5],[3,6],[6,5],[7,2],[7,8],[8,9],[9,7]]

g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])

v=[False for i in range(n+1)]
dfsv=[False for i in range(n+1)]

for i in range(1,n+1):
    if v[i]==False:
        if(checkCycle(i,-1)):
            print("Yes cycle is there")
            break