"""
Best time to buy and sell stock
7 1 5 3 6 4
Buy at 1 and sell at 6 => Profit: (6-1)=5
For each day, the minimum of previous days gives the max profit on that particular day
For 6, minimum among previous days is 1
"""

def f():
    mini=arr[0]
    profit=0
    for i in range(1,len(arr)):
        t=arr[i]-mini
        profit=max(profit,t)
        mini=min(mini,arr[i])
    return profit

arr=[7,1,5,3,6,4]
print(f())

def f():
    mini=[arr[0]]
    profit=0
    for i in range(1,len(arr)):
        mini.append(min(arr[i],mini[i-1]))
    for i in range(len(arr)):
        profit=max(profit,arr[i]-mini[i])
    return profit

arr=[7,1,5,3,6,4]
print(f())