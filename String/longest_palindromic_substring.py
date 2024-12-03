def longestPalindrome(A):
    n = len(A)
    if (n < 2):
        return A
    s=0
    maxi = 1
    for i in range(n):
        l = i-1
        h = i+1
        while(h<n and A[h]==A[i]):
            h+=1
        while(l>=0 and A[l]==A[i]):
            l-=1
        while(l>=0 and h<n and A[l]==A[h]):
            l-=1
            h+=1
        length=h-l-1
        if(maxi<length):
            maxi=length
            s=l+1
    return A[s:s + maxi]
    