# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #reverse list
        def reverseList(head):
            cur = head
            newHead = None
            while cur:
                tmp = cur.next
                cur.next = newHead
                newHead = cur
                cur = tmp
            return newHead

        #convert l1 to integer
        l1_reversed = reverseList(l1)
        l1_str = ""
        while l1_reversed:
            l1_str += str(l1_reversed.val)
            l1_reversed = l1_reversed.next

        #convert l2 to integer
        l2_reversed = reverseList(l2)
        l2_str = ""

        while l2_reversed:
            l2_str += str(l2_reversed.val)
            l2_reversed = l2_reversed.next

        total = int(l1_str) + int(l2_str)

        #deserialize
        if total == 0:
            return ListNode(0)

        head = ListNode(0)
        cur = head

        while total > 0:
            last_digit = total % 10 
            tmp = ListNode(last_digit)
            cur.next = tmp
            cur = cur.next
            total //= 10
        return head.next


        

        
