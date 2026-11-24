"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}
        def dfs(n):
            new = Node(n.val)
            oldToNew[n] = new
            for neigh in n.neighbors:
                if neigh not in oldToNew:
                    oldToNew[n].neighbors.append(dfs(neigh))
                else:
                    oldToNew[n].neighbors.append(oldToNew[neigh])
            return new
        dfs(node)
        return oldToNew[node]
