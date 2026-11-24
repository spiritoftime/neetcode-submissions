# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isHeightBalanced(root):
            if not root: return [0, True]
            l, lBalanced = isHeightBalanced(root.left)
            r,rBalanced = isHeightBalanced(root.right)

            if abs(l-r) > 1 or not lBalanced or not rBalanced:
                return [0,False]
            return [max(l,r) + 1, True]
        return isHeightBalanced(root)[1]
            