# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        imd = 0
        # move right n steps ahead (i.e. n nodes traversed)
        while imd < n:
            imd += 1
            right = right.next
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        # assume left is one node before the one to be deleted
        left.next = left.next.next
        return head
        
