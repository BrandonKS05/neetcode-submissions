# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        newlist = []
        cur = head
        while cur:
            newlist.append(cur)
            cur = cur.next
        print(newlist)
        l = 0
        r = len(newlist)-1
        while l < r -1:
            newlist[l].next = newlist[r]
            l += 1
            newlist[r].next = newlist[l]
            r -= 1
            newlist[l].next = newlist[r]
        newlist[r].next = None

        