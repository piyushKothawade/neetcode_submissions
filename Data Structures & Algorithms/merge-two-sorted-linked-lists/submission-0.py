# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # let's merge by creating a new node
        newHead = ListNode(-1)
        temp = newHead
        temp1, temp2 = list1, list2
        while temp1 and temp2:
            # compare
            if temp1.val < temp2.val:
                temp.next = temp1
                temp = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp = temp2
                temp2 = temp2.next
        if temp1:
            temp.next = temp1
        else:
            temp.next = temp2
        return newHead.next
        