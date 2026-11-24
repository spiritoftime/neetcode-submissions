# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        curr = head
        before = None
        while curr is not None:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        return before
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast = head,head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        l2 = prev.next
        prev.next = None



        reversed_l2 = self.reverseList(l2)
        c1,c2 = head,reversed_l2

        # [2,4], [10, 8, 6]
        #merge the two lists
        while c1 and c2:
            tmp1 = c1.next
            c1.next = c2
            tmp2 = c2.next
            if tmp1:
                c2.next = tmp1
            c1 = tmp1
            c2 = tmp2







