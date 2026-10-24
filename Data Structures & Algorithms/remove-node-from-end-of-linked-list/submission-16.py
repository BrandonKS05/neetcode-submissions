# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if not head:
            return None
        l = 0
        r = 1
        del nodes[len(nodes)-n]
        if not nodes:
            return None
        while l<len(nodes)-1:
            nodes[l].next = nodes[r]
            l+=1
            r+=1
        nodes[l].next = None
        return nodes[0]
        
            

