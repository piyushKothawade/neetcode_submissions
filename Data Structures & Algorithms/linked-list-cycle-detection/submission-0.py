# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = dict()
        temp = head
        while(temp):
            if temp in visited:
                return True
            else:
                visited[temp] = True
            temp = temp.next
        return False
