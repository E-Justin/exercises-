from typing import List


prices = [7,1,5,3,6,4]

def maxProfit(prices: List[int])-> int:
    if type(prices) is not list: # if argument type is not a list
        return 0
    total = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]: # if the next day's price is higher than the current (buy)
            total += (prices[i + 1] - prices[i]) # get profit
    
    return total # return profit

print(maxProfit(prices))
