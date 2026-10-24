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
            dummy = ListNode(0)
            dummy.next = newHead
            dummy = dummy.next
            return dummy

        #convert l1 to integer
        l1_reversed = reverseList(l1)
        l1_num = []
        while l1_reversed:
            l1_num.append(l1_reversed.val)
            l1_reversed = l1_reversed.next

        #convert l2 to integer
        l2_reversed = reverseList(l2)
        l2_num = []
        while l2_reversed:
            l2_num.append(l2_reversed.val)
            l2_reversed = l2_reversed.next

        total = int("".join(str(x) for x in l1_num)) + int("".join(str(x) for x in l2_num))
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


        

        
