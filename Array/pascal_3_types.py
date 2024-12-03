"""
Pascal triangle
"""

#1) Finding the entire pascal triangle
def solve(A):
    pas=[]
    if A==0:
        return pas
    if A==1:
        pas.append([1])
        return pas
    pas.append([1])
    pas.append([1,1])
    for i in range(2,A):
        a=[1]
        for j in range(1,i):
            a.append(pas[i-1][j]+pas[i-1][j-1])
        a.append(1)
        pas.append(a)
    return pas

print(solve(8))

#2) Finding an element of pascal triangle based on row and column numbers: r-1 C c-1
def fac(n):
    s=1
    for i in range(2,n+1):
        s*=i
    return s
r=6
c=4
print(fac(r-1)//(fac(c-1)*fac(r-c-2)))

#3) Find nth row
"""
if we need to find for 4th row
3C0, 3C1, 3C2, 3C3
3C1 = 3/1
3C2 = 3*2/1*2
3C3 = 3*2*2/1*2*3
Number of elements in the denominator = number of elements in numerator
"""
n=4
r=[1]
for i in range(1,n+1):
    r.append(r[i-1]*(n+1-i)//i)
print(r)