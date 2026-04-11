# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the LL
        len = 0
        curr = head
        while curr:
            curr = curr.next
            len += 1
        # delete the nth node from the end
        imd = 0
        curr = head
        while imd < len - n - 1:
            curr = curr.next
            imd += 1
        if len - n - 1 < 0:
            return head.next
        curr.next = curr.next.next
        return head

        
