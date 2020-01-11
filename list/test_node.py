import unittest
from .node import ListNode

class Test(unittest.TestCase):

    def test_linked_list_from_empty_list(self):
        head = ListNode.from_list([])
        self.assertIsNone(head)

    def test_linked_list_from_list(self):
        head = ListNode.from_list([1, 2, 3])
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)

    def test_linked_list_to_list(self):
        head = ListNode.from_list([1, 2, 3])
        self.assertListEqual(head.to_list(), [1, 2, 3])
