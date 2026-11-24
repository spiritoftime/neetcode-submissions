# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        # sever the 2nd half from the 1st half
        fast = slow.next
        slow.next = None
        # reverse 2nd half
        before =None
        while fast:
            after = fast.next
            fast.next = before
            before = fast
            fast = after
        # reorder the 2 lists
        l1,l2 = head, before
        while l2:
            t1 = l1.next
            l1.next = l2
            l1 = t1

            t2 = l2.next
            l2.next = l1
            l2 = t2
