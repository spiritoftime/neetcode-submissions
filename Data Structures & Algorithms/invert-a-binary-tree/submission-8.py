# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stack
        st = [root]
        while st:
            r = st.pop()
            if r:
                r.left,r.right = r.right,r.left
            if r and r.left:
                st.append(r.left)
            if r and r.right:
                st.append(r.right)
        return root