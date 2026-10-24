# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        status, counter = False, 0
        while cur:
            if cur.val > 1000:
                status = True
                break
            cur.val = cur.val + 2000
            counter += 1
            cur = cur.next
        

        cur = head
        
        for i in range(counter):
            cur.val = cur.val - 2000
            cur = cur.next
        return status

        