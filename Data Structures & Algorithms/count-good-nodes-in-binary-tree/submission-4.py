# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxEncountered):
            nonlocal res
            if not root:
                return 0
            if root.val >= maxEncountered:
                res +=1
            dfs(root.left, max(maxEncountered, root.val))  
            dfs(root.right,max(maxEncountered, root.val))
            return

        dfs(root, float('-inf'))
        return res