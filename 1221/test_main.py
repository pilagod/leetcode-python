import unittest
from .main import Solution

class Test(unittest.TestCase):

    def test_empty_string(self):
        self.assert_balanced_string_split('', 0)

    def test_split_balanced_string(self):
        self.assert_balanced_string_split('RL', 1)
        self.assert_balanced_string_split('RLRRLLRLRL', 4)
        self.assert_balanced_string_split('RLLLLRRRLR', 3)
        self.assert_balanced_string_split('LLLLRRRR', 1)

    def assert_balanced_string_split(self, s: str, expected: int):
        result = Solution().balancedStringSplit(s)
        self.assertEqual(result, expected)
