from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        # i -> has already performed i transactions

        # buy exactly i stocks at day
        hold_stock[i][day] = max(
            non_hold_stock[i-1][day-1] - prices[day], 
            hold_stock[i][day-1]
        ) 
        
        # buy and sell exactly i stocks at day
        non_hold_stock[i][day] = max(
            hold_stock[i][day-1] + prices[day], 
            non_hold_stock[i][day-1]
        )
        """
        if len(prices) <= 1:
            return 0
        if k >= len(prices)/2:
            return sum(prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i])
        result = 0
        # at most 0 transaction
        non_hold_stock_prev = [0] * (len(prices)+1) 
        for _ in range(k):
            hold_stock = [-float('inf')] * (len(prices) + 1)
            non_hold_stock = [-float('inf')] * (len(prices)+1)
            for i, p in enumerate(prices):
                day = i + 1
                hold_stock[day] = max(non_hold_stock_prev[day-1] - p, hold_stock[day-1])
                non_hold_stock[day] = max(hold_stock[day-1] + p, non_hold_stock[day-1])
            result = max(result, non_hold_stock[-1])
            non_hold_stock_prev = non_hold_stock
        return result
