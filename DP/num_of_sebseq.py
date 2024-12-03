#Using pick and non pick
def f(ind,d,m):
    if d==t:
        return 1
    if ind==len(s):
        if d==t:
            return 1
        return 0
    d+=s[ind]   
    l=f(ind+1,d,m)
    d=d[:len(d)-1]
    r=f(ind+1,d,m)
    return l+r

s="rabbbit"
t="rabbit"
d=""
m={}
print(f(0,d,m))

#Using comparision at each step
def f(m,n):
    if((m==0 and n==0) or n==0):
        return 1
    if(m==0):
        return 0
    if(s[m-1]==t[n-1]):
        l=f(m-1,n-1)
        r=f(m-1,n)
        return l+r
    else:
        return f(m-1,n)

s="rabbbit"
t="rabbit"
print(f(len(s),len(t)))

#Using memorization
def f(m,n):
    if((m==0 and n==0) or n==0):
        return 1
    if(m==0):
        return 0
    if(dp[m][n]!= -1):
        return dp[m][n]
    if(s[m-1]==t[n-1]):
        l=f(m-1,n-1)
        r=f(m-1,n)
        dp[m][n]=l+r
        return l+r
    else:
        l=f(m-1,n)
        dp[m][n]=l
        return l

s="rabbbit"
t="rabbit"
dp = [[-1 for j in range(len(t)+1)] for i in range(len(s)+1)]
print(f(len(s),len(t)))
