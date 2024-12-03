"""
Palidrome partitioning
s="aab" => [["a","a","b"],["aa","b"]]
Every partiton should be a string
"""

def isPalindrome(s):
    return s==s[::-1]
def f(A,ind,ds):
    if(ind==len(A)):
        x=ds.copy()
        ans.append(x)
        return
    for i in range(ind,len(A)):
        if(isPalindrome(A[ind:i+1])):
            ds.append(A[ind:i+1])
            f(A,i+1,ds)
            ds.pop()
            
ans=[]
f("aab",0,[])
print(ans)