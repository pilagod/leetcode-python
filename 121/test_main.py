import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):

    def test_empty_price(self):
        self.assert_max_profit([], 0)

    def test_one_price(self):
        self.assert_max_profit([9], 0)

    def test_multiple_prices(self):
        self.assert_max_profit([7, 1, 5, 3, 6, 4], 5)
        self.assert_max_profit([7,6,4,3,1], 0)

    def assert_max_profit(self, prices: List[int], expected: int):
        result = Solution().maxProfit(prices)
        self.assertEqual(result, expected)
