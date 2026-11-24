# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        left = dummyNode
        end = head
        for i in range(n):
            end = end.next
        while end:
            left,end = left.next,end.next
        left.next = left.next.next
        return dummyNode.next




        