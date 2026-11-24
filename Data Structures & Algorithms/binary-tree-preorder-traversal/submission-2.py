# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st, res = [], []
        curr = root
        while st or curr:
            while curr is not None:
                res.append(curr.val)
                if curr.right is not None:
                    st.append(curr.right)
                curr = curr.left
            curr = st.pop() if st else None
        return res