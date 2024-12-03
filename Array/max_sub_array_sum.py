"""
Kadane algorithm 
Maximum sub array sum
"""

arr=[1,3,-3,2]
maxi=float('-inf')
maxi_sub=0
for i in arr:
    maxi_sub+=i
    if(maxi_sub>maxi):
        maxi=maxi_sub
    if(maxi_sub<0):
        maxi_sub=0
print(maxi)
    