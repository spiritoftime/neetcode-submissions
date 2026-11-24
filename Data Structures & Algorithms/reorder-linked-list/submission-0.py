# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # needed for when you reverse linked list, curr1 and curr2 both point to the reversed list.
    def createNewList(self,head):
        new = curr = ListNode()
        tmp = head
        while tmp:
            curr.next = ListNode(tmp.val)
            curr = curr.next
            tmp = tmp.next
        return new
    def reverseLinkedList(self,head):
        before = None
        curr = head
        while curr:
            after  = curr.next
            curr.next = before
            before= curr
            curr = after
        return before
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse linked list
        #terminate condition: if curr1 == curr2
        curr1 = head
        curr2 = self.reverseLinkedList(self.createNewList(head))
        curr1Turn = True
        while curr1.val != curr2.val:
            if curr1Turn:
                tmp = curr1.next
                curr1.next = curr2
                curr1 = tmp                
            else:
                tmp = curr2.next
                curr2.next = curr1
                curr2 = tmp
            curr1Turn = not curr1Turn
        if curr1Turn:
            curr1.next = None
        else:
            curr2.next = None
        return curr1


        