# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        st = []
        curr = root
        while st or curr:
            while curr:
                st.append(curr)
                res.append(curr.val)

                curr = curr.left
            tmp = st.pop()
            if tmp.right:
                curr = tmp.right
        return res

