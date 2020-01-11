import unittest
from typing import List
from .main import Solution

class Test(unittest.TestCase):

    def test_total_prices(self):
        self.assert_max_profit(10, [7, 1, 5, 3, 6], 7)

    def test_multiple_prices(self):
        self.assert_max_profit(2, [2, 4, 1], 2)
        self.assert_max_profit(2, [3, 2, 6, 5, 0, 3], 7)
        self.assert_max_profit(2, [3, 2, 6, 5, 0, 3], 7)
        self.assert_max_profit(2, [2, 1, 2, 0, 1], 2)


    def assert_max_profit(self, k: int, prices: List[int], expected: int):
        result = Solution().maxProfit(k, prices)
        self.assertEqual(result, expected)
