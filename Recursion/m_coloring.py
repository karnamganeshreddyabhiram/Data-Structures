def safe(c,node):
    for i in g[node]:
        if col[i]==c:
            return False
    return True

def solve(node,n,m):
    if(node>=n):
        return True
    for i in range(1,m+1):
        if(safe(i,node)):
            col[node]=i
            if(solve(node+1,n,m)):
                return True
            col[node]=0
    return False

n=3
e=[[0,1],[0,2],[0,3],[1,3],[1,2]]
g=[[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
col = [0 for i in range(n+1)]
print(solve(0,n,3))