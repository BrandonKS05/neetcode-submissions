import ctypes
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import ctypes

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        add = []
        cur = head
        while cur:
            add.append(id(cur))
            cur = cur.next

        new_head = ctypes.cast(add[-1], ctypes.py_object).value

        for i in range(len(add) - 1, 0, -1):
            node = ctypes.cast(add[i], ctypes.py_object).value
            node.next = ctypes.cast(add[i - 1], ctypes.py_object).value

        ctypes.cast(add[0], ctypes.py_object).value.next = None
        return new_head