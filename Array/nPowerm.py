"""
Power of a number
n**m
if m is even 
2**4 => (4*4)**2 => n=n*n, m=m//2
if m is odd
2**3 => 2*(2)**2 => ans=ans*x, m=m-1
"""

n=2
m=10
ans=1
while(m):
    if(m%2==0):
        n=n*n
        m=m//2
    else:
        ans=ans*n
        m-=1
print(ans)
        
