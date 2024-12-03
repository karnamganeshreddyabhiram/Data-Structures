"""
2 sum
2 numbers in an array which adds to the target value
"""

arr=[1,2,3,4]
t=3
d={}
for i in arr:
   c=t-i
   if c in d:
       print(c,i)
   else:
       d[i]=1
       
        
       