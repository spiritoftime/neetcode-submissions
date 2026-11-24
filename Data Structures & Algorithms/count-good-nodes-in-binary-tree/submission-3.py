# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_encountered):
            if not root:
                return 0
            res = 0
            if root.val >= max_encountered:
                res += 1
            res += dfs(root.left, max(root.val, max_encountered))
            res += dfs(root.right, max(root.val, max_encountered))
            return res

        return dfs(root, float("-inf"))
