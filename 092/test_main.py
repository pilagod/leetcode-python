import unittest
from typing import List
from .main import ListNode, Solution

class Test(unittest.TestCase):

    def test_linked_list_from_empty_list(self):
        head = ListNode.from_list([])
        self.assertIsNone(head.val)
        self.assertIsNone(head.next)

    def test_linked_list_from_list(self):
        head = ListNode.from_list([1, 2, 3])
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)

    def test_linked_list_to_list(self):
        head = ListNode.from_list([1, 2, 3])
        self.assertListEqual(head.to_list(), [1, 2, 3])

    def reverse(self, values: List[int], m: int, n: int, expected: List[int]) :
        head = ListNode.from_list(values)
        result = Solution().reverseBetween(head, m, n)
        self.assertListEqual(result.to_list(), expected)

    def test_reverse_list(self):
        self.reverse([1, 2, 3, 4, 5], 1, 1, [1, 2, 3, 4, 5])
        self.reverse([1, 2, 3, 4, 5], 5, 5, [1, 2, 3, 4, 5])
        self.reverse([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
        self.reverse([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5])
        self.reverse([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3])
        