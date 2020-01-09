from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        profit = 0
        for p in prices[1:]:
            if p < buy:
                buy = p
                continue
            profit = max(profit, p - buy)
        return profit
            
            
