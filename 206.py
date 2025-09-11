# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        curr2 = head
        if not head:
            return head

        while curr2:
            tmp = curr2.next
            curr2.next =curr
            curr = curr2
            curr2 = tmp
        
        return curr