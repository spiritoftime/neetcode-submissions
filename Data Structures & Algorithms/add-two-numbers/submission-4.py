# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p_1 = l1
        c1,c2 = l1,l2
        while c1 and c2:
            total = c1.val + c2.val + carry
            carry = total // 10
            total  = total % 10
            c1.val = total
            p_1 = c1
            c1 = c1.next
            c2 = c2.next
        remaining = c2 or c1
        while remaining:
            total = remaining.val + carry
            carry= total // 10
            total = total % 10
            remaining.val = total
            p_1.next = remaining
            p_1 = remaining
            remaining = remaining.next
        if carry:
            p_1.next = ListNode(carry)
        return l1



