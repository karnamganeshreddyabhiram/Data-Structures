def isPalindrome(str,i,n):
    if(i>=n//2):
        return True
    if(str[i]!=str[n-i-1]):
        return False
    return isPalindrome(str,i+1,n)
print(isPalindrome("madam", 0, 5))