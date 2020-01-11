from __future__ import annotations
from typing import List, Type, Union

class ListNode:

    @classmethod
    def from_list(cls: Type[ListNode], values: List[int]) -> Union[ListNode, None]:
        if len(values) == 0:
            return None
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
