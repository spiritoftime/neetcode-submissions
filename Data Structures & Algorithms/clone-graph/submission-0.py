"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.oldToNew = {}
        if not node:return None
        def dfs(currNode):
            if currNode not in self.oldToNew:
                newNode = Node(currNode.val)
                self.oldToNew[currNode] = newNode
            else:
                return self.oldToNew[currNode]

            for neigh in currNode.neighbors:
                    dfs(neigh)
                    self.oldToNew[currNode].neighbors.append(self.oldToNew[neigh])
        dfs(node)
        return self.oldToNew[node]
        