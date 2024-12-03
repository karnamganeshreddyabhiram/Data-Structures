"""
https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
"""

#Using recursion
def f(day,last):
    if(day==0):
        maxi=grid[0][0]
        for i in range(len(grid[0])):
            if(i!=last):
                maxi=max(maxi,grid[0][i])
        return maxi
    maxi=0
    for i in range(len(grid[day])):
        if i!=last:
            maxi=max(f(day-1,i)+grid[day][i],maxi)
    return maxi

grid=[
      [2,1,3],
      [3,4,5],
      [10,1,6],
      [8,3,7]]

print(f(3,-1))

#Using memorization
def f(day,last,dp):
    if(day==0):
        maxi=grid[0][0]
        for i in range(len(grid[0])):
            if(i!=last):
                maxi=max(maxi,grid[0][i])
        dp[day][last]=maxi
        return maxi
    if(dp[day][last]!=-1):
        return dp[day][last] 
    maxi=0
    for i in range(len(grid[day])):
        if i!=last:
            maxi=max(f(day-1,i,dp)+grid[day][i],maxi)
    dp[day][last]=maxi
    return maxi

grid=[
      [2,1,3],
      [3,4,5],
      [10,1,6],
      [8,3,7]]
dp=[[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
print(f(3,-1,dp))

#Using tabulation
def f(dp):
    dp[0][0]=max(grid[0][1],grid[0][2])
    dp[0][1]=max(grid[0][0],grid[0][2])
    dp[0][2]=max(grid[0][0],grid[0][1])
    dp[0][3]=max(grid[0][0],grid[0][1],grid[0][2])
    
    for day in range(1,len(grid)):
        for last in range(4):
            dp[day][last]=0
            maxi=0
            for i in range(len(grid[day])):
                if(i!=last):
                    maxi=max(maxi,dp[day-1][i]+grid[day][i])
            dp[day][last]=maxi
    return dp[len(grid)-1][3]

grid=[
      [10,40,70],
      [20,50,80],
      [30,60,90]]
dp=[[-1 for i in range(len(grid[0])+1)] for j in range(len(grid))]
print(f(dp))

                
        