st=[1,0,3,8,5,8]
fi=[2,6,4,9,7,9]
arr=[]
for i in range(len(st)):
    arr.append([st[i],fi[i],i])
arr=sorted(arr, key=lambda x:x[1])
ans=[arr[0][2]+1]
p=arr[0][1]
for i in range(1,len(st)):
    if arr[i][0]>p:
        ans.append(arr[i][2]+1)
        p=arr[i][2]
print(ans)