def stock_buy_and_sell(arr):
    n = len(arr)
    mini = arr[0]
    profit = 0
    for i in range(1,n):
        cost = arr[i] - mini
        profit = max(profit,cost)
        mini = min(mini,arr[i])
    return profit 
arr = [7,1,5,3,6,4]
print(stock_buy_and_sell(arr))    # T.C. = O(N) and S.C. = O(1)