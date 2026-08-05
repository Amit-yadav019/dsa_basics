def stock_buy_and_sell(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0,n):

        for j in range(i+1,n):
            if prices[j] > prices[i]:
                p = prices[j] - prices[i]
                max_profit = max(max_profit,p)
              
    return max_profit
prices = [7,2,1,5,6,4,8]
print("The max. profit is : ", stock_buy_and_sell(prices))
            
            
