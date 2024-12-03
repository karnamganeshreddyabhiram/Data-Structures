def lenghtOfLongestAP(A, n) :
 
    # Stores the length of sequences
    # having same difference
 
    # Stores the resultant length
    res = 2
 
    # Iterate over the array
    for i in range(n) :
 
        for j in range(i + 1, n) :
 
            d = A[j] - A[i]
 
            # Update length of subsequence
            if d in dp :
                if i in dp[d] :
                    dp[d][j] = dp[d][i] + 1
                else :
                    dp[d][j] = 2
            else :
                dp[d] = {}
                dp[d][j] = 2
 
            if d in dp :
                if j in dp[d] :
                    res = max(res, dp[d][j])
 
    # Return res
    return res
 
# Given array arr[]
arr = [ 20, 1, 15, 3, 10, 5, 8 ]
 
N = len(arr)
dp = {} 
# Function Call
print(lenghtOfLongestAP(arr, N))