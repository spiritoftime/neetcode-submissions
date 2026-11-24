# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self,root):
        if not root:
            return 0
        return max(self.getHeight(root.left),self.getHeight(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            if abs(leftHeight - rightHeight) > 1:
                return False
            return dfs(root.left) and dfs(root.right)

        return dfs(root)
            
        