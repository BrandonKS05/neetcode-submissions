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
    
        
        rev = None
        while head:
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        return rev


        

        

        