arr=[1,3,8,-1,-3,30,10,12]
maxi_all=0
maxi_until=0
for i in arr:
    maxi_until+=i
    if maxi_all<maxi_until:
        maxi_all=maxi_until
    if maxi_until<0:
        maxi_until=0
print(maxi_all)
