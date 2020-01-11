from typing import List

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs: List[int] = []
        for s_char, t_char in zip(s, t):
            costs.append(abs(ord(s_char) - ord(t_char)))
        result, w_anchor, w_cost = 0, 0, 0
        for i, cost in enumerate(costs):
            w_cost += cost
            while w_anchor <= i and w_cost > maxCost:
                w_cost = w_cost - costs[w_anchor]
                w_anchor += 1
            result = max(result, i - w_anchor + 1)
        return result