def f(n,k):
    if(n==0):
        return 0
    return (f(n-1,k)+k)%n

print(f(14,2))