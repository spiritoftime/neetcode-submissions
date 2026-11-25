"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        # old node to new node
        if not node: return 
        def dfs(n):
            if not n: return
            newNode = Node(n.val)
            oldToNew[n] = newNode

            for neigh in n.neighbors:
                if neigh in oldToNew:
                    newNode.neighbors.append(oldToNew[neigh])

                else:
                    dfs(neigh)
                    newNode.neighbors.append(oldToNew[neigh])


        dfs(node)
        return oldToNew[node]