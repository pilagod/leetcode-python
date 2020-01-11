from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result: List[List[int]] = []
        ns = sorted(nums)
        for i, n in enumerate(ns):
            if i > 0 and ns[i] == ns[i-1]:
                continue
            target, l, r = 0-n, i+1, len(ns)-1
            while l < r:
                s = ns[l] + ns[r]
                if s == target:
                    result.append([n, ns[l], ns[r]])
                    l += 1
                    r -= 1
                    while l < r and ns[l] == ns[l-1]:
                        l += 1
                    while l < r and ns[r] == ns[r+1]:
                        r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return result