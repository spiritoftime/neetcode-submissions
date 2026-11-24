"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return node
        oldToNew = {}
        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            oldToNew[n] = Node(n.val)
            for neigh in n.neighbors:
                neigh_node = dfs(neigh)
                oldToNew[n].neighbors.append(neigh_node)
            return oldToNew[n]
        dfs(node)
        return oldToNew[node]