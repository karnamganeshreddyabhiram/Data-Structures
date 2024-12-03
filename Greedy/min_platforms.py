arr=[900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()
plat=1
res=1
i=1
j=0
while(i<len(arr) and j<len(arr)):
    if arr[i]<=dep[j]:
        plat+=1
        i+=1
    else:
        j+=1
        plat-=1
    res=max(res,plat)
print(res)
        