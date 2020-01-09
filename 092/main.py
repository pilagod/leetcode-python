from __future__ import annotations
from typing import List, Type, Union

# Definition for singly-linked list.

class ListNode:

    @classmethod
    def from_list(cls: Type[ListNode], values: List[int]) -> ListNode:
        if len(values) == 0:
            return cls(None)
        head = cur = cls(values[0])
        for value in values[1:]:
            cur.next = cls(value)
            cur = cur.next
        return head

    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self) -> List[int]:
        result: List[int] = []
        result.append(self.val)
        cur = self.next
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i, cur, prev = 0, head, None
        m_node, m_prev_node = None, None
        n_node, n_next_node = None, None
        while cur is not None:
            i += 1
            if m-1 == i:
                m_prev_node = cur
            if m == i:
                m_node = cur
            if n == i:
                n_node = cur
            if n+1 == i:
                n_next_node = cur
            if m < i <= n:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            else:
                prev = cur
                cur = cur.next
        m_node.next = n_next_node
        if m_prev_node is not None:
            m_prev_node.next = n_node
        return head if m_prev_node is not None else n_node