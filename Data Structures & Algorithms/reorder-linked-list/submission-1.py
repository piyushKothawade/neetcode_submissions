# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # how to find the middle?
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow denotes the middle of the LL
        # reverse the second half
        secHalf = slow.next
        def solve(head):
            if head is None or head.next is None:
                return head
            # reverse the rest of the linked list
            newHead = solve(head.next)
            head.next.next = head
            head.next = None
            return newHead
        secHead = solve(secHalf)
        slow.next = None

        t1 = head
        t2 = secHead
        while t1 and t2:
            t1Next = t1.next
            t2Next = t2.next
            t1.next = t2
            t2.next = t1Next
            t1 = t1Next
            t2 = t2Next
        




        
        
        