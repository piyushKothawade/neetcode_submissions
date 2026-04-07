# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(head):
            if head is None or head.next is None:
                return head
            # reverse the rest of the linked list
            newHead = solve(head.next)
            head.next.next = head
            head.next = None
            return newHead
        return solve(head)