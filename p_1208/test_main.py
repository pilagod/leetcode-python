import unittest
from .main import Solution

class Test(unittest.TestCase):

    def test_equal_substring(self):
        self.assert_equal_substring('abcd', 'efgh', 0, 0)
        self.assert_equal_substring('abcd', 'abef', 0, 2)
        self.assert_equal_substring('abcd', 'bcdf', 3, 3)
        self.assert_equal_substring('abcd', 'cdef', 3, 1)
        self.assert_equal_substring('abcd', 'wxyz', 3, 0)
        self.assert_equal_substring('abcd', 'abcdwjeorijdfgmlk', 3, 4)

    def assert_equal_substring(self, s: str, t: str, cost: int, expected: int):
        result = Solution().equalSubstring(s, t, cost)
        self.assertEqual(result, expected)
