# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #head -> node1 next -> node2 next -> node3
        #rev -> None

       
        # rev = None
        # while True:
        #     if head is None:
        #         return rev
        #     rev = ListNode(head.val, rev)
        #     head = head.next
    
        cur = head
        rev = None
        while cur:
            temp = cur.next
            cur.next = rev
            rev = cur
            cur = temp
        return rev


        

        

        