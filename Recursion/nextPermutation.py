a="13542"
n=len(a)
x=n-1
for i in range(n-2,-1,-1):
    if a[i]<a[i+1]:
        x=i
        break
y=x
while(y<n and a[x]<=a[y]):
    y+=1
y-=1
l1=list(a)
l1[x],l1[y]=l1[y],l1[x]
a=''.join(l1)
a=a[:x+1]+a[x+1:][::-1]
print(a)