#Recursion, Memorization -> Top down
#Tabulation -> Bottom to Top
def fibo(n,dp):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]

n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))