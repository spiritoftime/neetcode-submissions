# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        c1,c2 = list1, list2

        while c1 and c2:
            if c1.val < c2.val: # add c1 first
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
        if c1: # remaining nodes at c1
            curr.next = c1
        if c2:
            curr.next = c2
        return dummy.next