from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        # calculate diffs            
        buy, prev = prices[0], prices[0]
        diffs: List[int] = []
        for p in prices[1:]:
            if p <= prev:
                diffs.append(prev-buy)
                diffs.append(p-prev)
                buy = p
            prev = p
        # patch last ascending diff
        if prices[-1] > buy:
            diffs.append(prices[-1]-buy)
        # prices are all ascending
        if len(diffs) == 1: 
            return diffs[0]
        # calculate max profits from start for each segment
        acc = 0
        profits_from_start = [0] * len(diffs)
        profits_from_start[0] = diffs[0]
        for i in range(0, len(diffs)):
            diff = diffs[i]
            acc += diff
            if acc < 0:
                acc = max(0, diff)
            profits_from_start[i] = max(acc, profits_from_start[i-1])
        # calculate max profits from end for each segment
        acc = 0
        profits_from_end = [0] * len(diffs)
        profits_from_end[-1] = max(0, diffs[-1])
        for i in range(len(diffs)-2, -1, -1):
            diff = diffs[i]
            acc += diff
            if acc < 0:
                acc = max(0, diff)
            profits_from_end[i] = max(acc, profits_from_end[i+1])
        # combine start and end segment
        result = 0
        for i in range(0, len(diffs)):
            if i == len(diffs) - 1:
                result = max(result, profits_from_start[i])
            else:
                result = max(result, profits_from_start[i] + profits_from_end[i+1])
        return result
        