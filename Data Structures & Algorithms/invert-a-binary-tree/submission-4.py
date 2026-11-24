# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            curr = stack.pop()
            l = curr.left
            r = curr.right
            curr.left, curr.right = r, l 
            if l:
                stack.append(l)
            if r:
                stack.append(r)
        return root