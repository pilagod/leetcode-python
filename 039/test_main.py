import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):
        
    def test_no_candidates(self):
        self.assert_combination_sum([], 1, [])

    def test_one_candidates(self):
        self.assert_combination_sum([1], 0, [])
        self.assert_combination_sum([1], 1, [[1]])
        self.assert_combination_sum([2], 1, [])

    def test_multiple_candidates(self):
        self.assert_combination_sum([2, 3, 6, 7], 7, [
            [2, 2, 3], 
            [7]
        ])
        self.assert_combination_sum([2, 3, 5], 8, [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ])

    def assert_combination_sum(self, candidates: List[int], target: int, expected: List[List[int]]):
        result = Solution().combinationSum(candidates, target)
        self.assertListEqual(result, expected)
