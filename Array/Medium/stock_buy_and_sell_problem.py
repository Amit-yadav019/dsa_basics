# in this problem we are allowed to buy once and sell once 

def buy_and_sell(arr):
    n = len(arr)
    mini = arr[0] 
    # Initially, consider the first price as the minimum price
    # that we have seen so far

    profit = 0 # Initially, we have made 0 profit
    
    for i in range(1,n): # Start from index 1 because arr[0] is already stored in mini
        cost = arr[i]- mini 
        profit = max(profit, cost)

        # Update the minimum price
        # Compare the previous minimum with today's price and keep whichever is smaller.

        mini = min(mini, arr[i])
    return profit 
arr = [6,7,2,4,10,1,22,7,3,23]
print(buy_and_sell(arr))

