def maxPerkItems(catridges, dollars, recycleReward,perksCost):
    maxi=0
    for i in range(catridges+1):
        x=dollars+(i*recycleReward)
        y=catridges-i
        maxi=max(maxi,min(x//perksCost,y))
    return maxi

c=3
d=6
rc=4
pc=5
print(maxPerkItems(c, d, rc, pc))