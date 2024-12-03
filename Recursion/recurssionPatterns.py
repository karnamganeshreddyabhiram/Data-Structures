def fun(a):
    if a==1:
        return 
    print(a)
    fun(a-1)
fun(10)

def fun1(n):
    if n==0:
        return
    print("Maruthi")
    fun1(n-1)
fun1(10)

def fun2(i,n):
    if i<1:
        return
    fun2(i-1,n)
    print(i)
fun2(3,3)

def fun3(i,n):
    if i>3:
        return
    fun3(i+1,n)
    print(i)
fun3(1,3)

def fun4(n):
    if(n==0):
        return 0
    return n+fun4(n-1)
print(fun4(4))