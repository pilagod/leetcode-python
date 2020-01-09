import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):

    def test_empty_price(self):
        self.assert_max_profit([], 0)

    def test_one_price(self):
        self.assert_max_profit([1], 0)

    def test_multiple_prices(self):
        self.assert_max_profit([3, 3], 0)
        self.assert_max_profit([3, 3, 5, 0, 0, 3, 1, 4], 6)
        self.assert_max_profit([1, 2, 3, 4, 5], 4)
        self.assert_max_profit([7, 6, 4, 3, 1], 0)
        self.assert_max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13)

    def assert_max_profit(self, prices: List[int], expected: int):
        result = Solution().maxProfit(prices)
        self.assertEqual(result, expected)
