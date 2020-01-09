import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):
    
    def test_three_sum_less_than_three_numbers(self):
        self.assert_three_sum([], [])
        self.assert_three_sum([0], [])
        self.assert_three_sum([0, 0], [])

    def test_three_sum(self):
        self.assert_three_sum([0, 0, 0], [
            [0, 0, 0]
        ])
        self.assert_three_sum([1, -1, 0], [
            [-1, 0, 1]
        ])
        self.assert_three_sum([-1, 0, 1, 2, -1, -4], [
            [-1, -1, 2],
            [-1, 0, 1]
        ])

    def assert_three_sum(self, numbers: List[int], expected: List[List[int]]):
        result = Solution().threeSum(numbers)
        self.assertListEqual(result, expected)
