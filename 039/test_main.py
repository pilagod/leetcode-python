import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):

    def solve(self, candidates: List[int], target: int, expected: List[List[int]]):
        result = Solution().combinationSum(candidates, target)
        self.assertListEqual(result, expected)
        
    def test_no_candidates(self):
        self.solve([], 1, [])

    def test_one_candidates(self):
        self.solve([1], 0, [])
        self.solve([1], 1, [[1]])
        self.solve([2], 1, [])

    def test_multiple_candidates(self):
        self.solve([2, 3, 6, 7], 7, [
            [2, 2, 3], 
            [7]
        ])
        self.solve([2, 3, 5], 8, [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ])