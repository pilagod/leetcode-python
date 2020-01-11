# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from time import sleep
from typing import cast, Optional, Tuple, Union
from list.node import ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return None
        if k == 1 or head.next is None:
            return head
        g_start, g_start_prev = None, None
        g_end = None
        g_count = 0
        cur, prev = head, None
        while cur is not None:
            g_count += 1
            if g_count == 1:
                g_start = cur
                g_start_prev = prev
            next = cur.next
            if g_count != k:
                prev = cur
                cur = next
                continue
            g_end = cur
            g_start, g_end = self.reverse(
                cast(ListNode, g_start), 
                cast(ListNode, g_end)
            )
            if g_start_prev is None:
                head = g_start
            else:
                g_start_prev.next = g_start
            g_end.next = next
            g_count = 0
            prev = g_end
            cur = next
        return head

    def reverse(self, head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
        cur, prev = head.next, head
        while cur is not None:
            next = cur.next
            cur.next = prev
            if cur == tail:
                break
            prev = cur
            cur = next
        return tail, head
