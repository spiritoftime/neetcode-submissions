# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and the hare:
        # set two pointers, fast and slow. they should never meet if no cycle
        # if there is cycle, they will meet.
        # its like 2.4km, the 15min guys never meet 7min guys.
        # however if it is in a track, they will lap you many times.

        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        