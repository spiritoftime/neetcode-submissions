# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        # get the 2nd half of the linked list at slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        before = slow.next = None
        # reverse linked list
        while secondHalf:
            after = secondHalf.next
            secondHalf.next = before
            before= secondHalf
            secondHalf = after
        # merge
        first,second = head,before
        while second: # it is always the smaller list
            tmp1 = first.next
            first.next = second
            first = tmp1

            tmp2 = second.next
            second.next = first
            second = tmp2

            




        