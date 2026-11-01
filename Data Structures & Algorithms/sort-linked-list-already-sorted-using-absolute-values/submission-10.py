# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:
        newhead = None
        tail = newhead
        
      
        while head and head.val < 0:
            tmp = head.next
            head.next = newhead
            if not newhead:
                tail = head
            newhead = head
            head = tmp

        cur = prev = head 
        while cur:
            if cur.val < 0:
                nxt = cur.next
                cur.next = newhead
                if not newhead:
                    tail = cur
                newhead = cur
                prev.next = nxt
                cur = nxt
                
            else: 
                prev = cur
                cur = cur.next
        
        
        if not newhead:
            return head
        else:
            tail.next = head
            return newhead


   
            
