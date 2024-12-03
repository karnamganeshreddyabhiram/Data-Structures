jobs=[[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
jobs=sorted(jobs, key=lambda x:x[2], reverse=True)
max_deadLine = 0
for i in jobs:
    max_deadLine=max(max_deadLine,i[1])
arr=[-1]*(max_deadLine+1)
arr[0]=0
n=len(jobs)
c_jobs=0
p_jobs=0
for i in range(n):
    for j in range(jobs[i][1],0,-1):
        if(arr[j]==-1):
            arr[j]=jobs[i][0]
            c_jobs+=1
            p_jobs+=jobs[i][2]
            break
print(arr,c_jobs,p_jobs)
    