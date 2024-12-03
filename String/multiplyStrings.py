def multiply(A, B):
    if A=="0" or B=="0":
        return "0"
    res = [0]*(len(A)+len(B))
    A,B=A[::-1],B[::-1]
    for i in range(len(A)):
        for j in range(len(B)):
            res[i+j]+=(int(A[i])*int(B[j]))
            res[i+j+1]+=res[i+j]//10
            res[i+j]%=10
    res=res[::-1]
    c=0
    while(c<len(res) and res[c]==0):
        c+=1
    res=res[c:]
    res=[str(i) for i in res]
    return ''.join(res)