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
        oldToNew = {}
        curr = head
        if not curr:
            return None
        while curr:
            if curr not in oldToNew:
                oldToNew[curr] = Node(curr.val)
            curr = curr.next
        copy_next = head
        while copy_next:
            ref_to_new = oldToNew.get(copy_next,None)
            ref_to_new.next = oldToNew.get(copy_next.next, None)
            ref_to_new.random = oldToNew.get(copy_next.random, None)
            copy_next = copy_next.next
        return oldToNew[head]