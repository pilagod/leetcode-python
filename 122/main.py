from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, prev = prices[0], prices[0]
        profit = 0
        for p in prices[1:]:
            if p <= prev:
                profit += prev - buy
                buy = p
            prev = p
        if prices[-1] > buy:
            profit += prices[-1] - buy
        return profit
