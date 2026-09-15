def buy_and_sell(arr):
    n = len(arr)
    mini = arr[0]
    profit = 0 
    
    for i in range(1,n):
        cost = arr[i]- mini 
        profit = max(profit, cost)
        mini = min(mini, arr[i])
    return profit 
arr = [6,7,2,4,10,1,22,7,3,23]
print(buy_and_sell(arr))

