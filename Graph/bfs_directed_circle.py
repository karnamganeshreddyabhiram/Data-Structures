n=5
e=[[4,0],[4,1],[3,1],[2,3],[5,2],[5,0]]

g = [[] for i in range(n+1)]
for i in e:
    g[i[0]].append(i[1])

inDegree = [0 for i in range(n+1)]
for i in e:
    inDegree[i[1]]+=1

q=[]
for i in range(len(inDegree)):
    if inDegree[i]==0:
        q.append(i)

cou=0
while(q):
    c=q.pop(0)
    cou+=1
    for i in g[c]:
        inDegree[i]-=1
        if(inDegree[i]==0):
            q.append(i)
            
if(cou==n+1):
    print("No cycle")
else:
    print("There is a cycle")