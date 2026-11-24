"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is  None:
            return None
        curr = head
        # copy next pointers
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
        curr = head
        # copy random pointers
        while curr:
            copied = curr.next
            copied.random = curr.random
            if curr.random is not None:
                copied.random = curr.random.next
            curr = curr.next.next # go to the next old node
        # detach old from new and restore old
        curr = head
        newHead = head.next
        while curr:
            newNode = curr.next
            curr.next = curr.next.next # attach old next back to old node
            newNode.next = newNode.next
            if newNode.next is not None:
                newNode.next = newNode.next.next
            curr = curr.next
        return newHead
