# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        def dfs(currMax,root):
            if not root:
                return
            if root.val >= currMax:
                self.goodNodes += 1
            currMax = max(currMax,root.val)
            dfs(currMax,root.left)
            dfs(currMax,root.right)
        dfs(float("-inf"),root)
        return self.goodNodes
        