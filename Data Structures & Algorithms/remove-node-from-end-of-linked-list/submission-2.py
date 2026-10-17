# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next
        
        place = count - n

        if place <= 0:
            return head.next
        
        prev = None
        curr = head 
        for i in range(place):
            prev = curr 
            curr = curr.next

        prev.next = curr.next

        return head