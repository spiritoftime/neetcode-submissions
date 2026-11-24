# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative method
        res = 0
        if not root:
            return 0
        stack = [(root,1)]
        while stack:
            currNode, currHeight = stack.pop()
            res = max(res, currHeight)
            if currNode.left:
                stack.append((currNode.left, currHeight + 1))
            if currNode.right:
                stack.append((currNode.right, currHeight + 1))
        return res      