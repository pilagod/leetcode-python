import unittest
from typing import List
from .main import ListNode, Solution


class Test(unittest.TestCase):

    def test_reverse_empty(self):
        self.assert_reverse_k_group([], 1, [])

    def test_reverse_one_group(self):
        self.assert_reverse_k_group([1, 2, 3], 1, [1, 2, 3])

    def test_reverse_two_group(self):
        self.assert_reverse_k_group([1], 2, [1])
        self.assert_reverse_k_group([1, 2], 2, [2, 1])
        self.assert_reverse_k_group([1, 2, 3], 2, [2, 1, 3])
        self.assert_reverse_k_group([1, 2, 3, 4], 2, [2, 1, 4, 3])
        self.assert_reverse_k_group([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])

    def test_reverse_multiple_groups(self):
        self.assert_reverse_k_group([1, 2, 3], 10, [1, 2, 3])
        self.assert_reverse_k_group([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
        self.assert_reverse_k_group([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4])

    def assert_reverse_k_group(self, values: List[int], k: int, expected: List[int]):
        head = ListNode.from_list(values)
        result: ListNode = Solution().reverseKGroup(head, k)
        if result is None:
            self.assertListEqual([], expected)
        else:
            self.assertListEqual(result.to_list(), expected)
