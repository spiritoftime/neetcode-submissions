# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before,curr = ListNode(), head
        dummy = before
        before.next = head
        for i in range(n):
            curr = curr.next
        while curr is not None:
            before = before.next
            curr = curr.next
        before.next = before.next.next
        return dummy.next
