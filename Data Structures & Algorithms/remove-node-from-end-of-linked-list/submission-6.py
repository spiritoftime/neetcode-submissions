# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # given curr (node to remove), you need to get the prev and the after
        # after can be derived from prev.next.next.
        # prev is the tricky part.
        # start by creating c1 and end, while end is not None advance c1 and end
        # c1 will end up with curr
        # Hence, you will need prev that lags behind curr 
        prev,curr, end = ListNode(), head, head
        res = prev
        prev.next = head
        for i in range(n):
            end = end.next
        while end is not None:
            end = end.next
            prev = curr
            curr = curr.next
        prev.next = prev.next.next
        return res.next

        # Method 2:
        # before,curr = ListNode(), head
        # dummy = before
        # before.next = head
        # for i in range(n):
        #     curr = curr.next
        # while curr is not None:
        #     before = before.next
        #     curr = curr.next
        # before.next = before.next.next
        # return dummy.next
