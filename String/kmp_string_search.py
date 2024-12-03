s="aabcaa"
pat="caa"
n = len(s)
lps = [0]*n
i,l = 1,0
while i < n:
    if s[i]==s[l]:
        lps[i] = l+1
        l+=1
        i+=1
    elif l > 0:
        l = lps[l-1]
    else:
        i+=1

txt=s
j=0
N=len(s)
M=len(pat)
i = 0
while i < N:
    if pat[j] == txt[i]:
        i += 1
        j += 1
    if j == M:
        print ("Found pattern at index " + str(i-j))
        j = lps[j-1]      
    elif i < N and pat[j] != txt[i]:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1