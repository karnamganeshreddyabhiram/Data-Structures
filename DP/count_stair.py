#Climbing stairs problem
"""
Find number of ways a person can climb to top of the stair if he can move either one or two steps up
each time
This problem is similar to fibonaci problem
Also similar to count number of ways recursion pattern
"""

def stairs(n):
    #If we reach the last step there is only one way
    if(n==0):
        return 1
    if(n==1):
        return 1
    #We can go 1 step back or 2 staps back
    l=stairs(n-1)
    r=stairs(n-2)
    #Both possibilities
    return l+r

stairs(3)



