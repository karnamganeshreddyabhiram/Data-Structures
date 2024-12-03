r,s=input().split(" ")
d=[0]*26
for i in r:
    d[ord(i)-ord('a')]+=1
for i in s:
    d[ord(i)-ord('a')]-=1
ans=0
for i in d:
    if(i!=0):
        ans+=abs(i)
print(ans//2)