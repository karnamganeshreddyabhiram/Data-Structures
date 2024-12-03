"""
Longest consecutive sequence
In an array find the longest consecutive sequence
a=[1,2,3,4,100,101,102,201]
1,2,3,4 answer is 4
"""
a=[1,2,3,4,100,101,102,201]
s=set()
for i in a:
    s.add(i)

maxi=0
for i in a:
    if i-1 not in s:
        c=1
        while(i+1 in s):
            c+=1
            i+=1
        maxi=max(maxi,c)
print(maxi)         
