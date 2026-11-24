# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we will check if it is balanced at every root
        # every function should return (maxHeight, isBalanced) so we can do one pass
        def dfs(root):
            if not root:
                return 0, True
            l,lBalanced = dfs(root.left)
            r,rBalanced = dfs(root.right)
            if not lBalanced or not rBalanced or abs(l-r) >1:
                return (max(l,r)+1, False)
            return (max(l,r)+1, True)
        return dfs(root)[1]
    
