# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root):
            nonlocal res
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
             # calculate root + 2 subroots, just itself, or just root + one subroot
            res = max(l+r + root.val, res, root.val, max(l,r) + root.val)
            # calculate new sbrootadd the subroot or just use root
            return max(max(l,r) + root.val, root.val) 
        dfs(root)
        return res