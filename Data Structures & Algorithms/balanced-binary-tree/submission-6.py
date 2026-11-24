# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(root):
            if not root:
                return 0
            l, r = maxHeight(root.left), maxHeight(root.right)
            return max(l, r) + 1

        def dfs(root):
            if not root:
                return True
            l, r = maxHeight(root.left), maxHeight(root.right)
            if abs(l - r) > 1:
                return False
            return dfs(root.left) and dfs(root.right)
        return dfs(root)   