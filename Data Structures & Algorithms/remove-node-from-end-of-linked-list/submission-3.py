# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # have three pointers, before, curr and end.
        # advance end by n amount of pointers. while end is not None(ie)
        # havent reached the end, advance before, curr and end.
        # before.next = curr.next
        # curr.next= None
        before,curr,end = ListNode(),head,head
        dummy = before
        before.next = head
        for i in range(n):
            end = end.next
        while end is not None:
            before = before.next
            curr = curr.next
            end = end.next
        before.next = curr.next
        curr.next = None
        return dummy.next