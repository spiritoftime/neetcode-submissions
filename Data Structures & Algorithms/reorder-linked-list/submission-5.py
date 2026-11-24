# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head,head
        # find the middle point- slow will be the middle/ last node of 1st half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next # start of 2nd half
        slow.next = None # detach the 2nd half
        # reverse the 2nd half
        reversed_ls = None
        while fast:
            after = fast.next
            fast.next = reversed_ls
            reversed_ls = fast
            fast = after

        # reorder the list
        first,second = head, reversed_ls
        while second:
            tmp1 = first.next
            first.next = second
            first = tmp1

            tmp2 = second.next
            second.next = first
            second = tmp2
        