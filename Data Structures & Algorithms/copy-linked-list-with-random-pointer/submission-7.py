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
        if not head: return None
        # 1 pass to populate oldToNew first
        oldToNew = {}
        c = head
        i = 0
        while c:
            oldToNew[c] = Node(c.val)
            c = c.next
        # populate the random and the next
        c = head
        while c:
            if c.next is not None:
                oldToNew[c].next = oldToNew[c.next]
            else:
                oldToNew[c].next = None
            if c.random is not None:
                oldToNew[c].random= oldToNew[c.random]
            else:
                oldToNew[c].random = None
            c = c.next
        return oldToNew[head]
