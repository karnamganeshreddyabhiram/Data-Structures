"""
Wildcard matching
? -> Single character
* -> Multi character
ab*f
abcdef
True
"""

#Using recursion
def f(i,j):
    if(i<0 and j<0):
        return True
    if(i<0 and j>=0):
        return False
    if(i>=0 and j<0):
        for k in range(i):
            if(s1[k]!="*"): #"***" == ""
                return False
        return True
    if(s1[i]==s2[j] or s1[i]=="?"):
        return f(i-1,j-1)
    if(s1[i]=="*"):
        return f(i-1,j) or f(i,j-1)
    return False

s1="ab*f"
s2="abcdef"
print(f(len(s1)-1,len(s2)-1))

#Using memorization
def f(i,j):
    if(i<0 and j<0):
        return True
    if(i<0 and j>=0):
        return False
    if(i>=0 and j<0):
        for k in range(i):
            if(s1[k]!="*"): #"***" == ""
                return False
        return True
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(s1[i]==s2[j] or s1[i]=="?"):
        dp[i][j]=f(i-1,j-1)
        return dp[i][j]
    if(s1[i]=="*"):
        dp[i][j]= f(i-1,j) or f(i,j-1)
        return dp[i][j]
    return False

s1="ab*f"
s2="abcdef"
dp=[[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f(len(s1)-1,len(s2)-1))

#Using tabulation
def f():
    dp[0][0]=True
    for i in range(1,len(s2)):
        dp[0][i]=False
    for i in range(1,len(s1)):
        f=True
        for k in range(i):
            if(s1[k]!="*"):
                f=False
                break
        dp[i][0]=f
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if(s1[i-1]==s2[j-1] or s1[i-1]=="?"):
                dp[i][j]=dp[i-1][j-1]
            elif(s1[i-1]=="*"):
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j]=False
    return dp[i][j]

s1="ab*f"
s2="abcdef"
dp=[[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
print(f())

    