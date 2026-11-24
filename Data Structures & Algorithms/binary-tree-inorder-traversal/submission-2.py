# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = []
        curr = root
        while st or curr:
            while curr is not None:
                st.append(curr)
                curr = curr.left
            tmp = st.pop()
            res.append(tmp.val)
            if tmp.right is not None:
                curr = tmp.right



        # recursive
        # def dfs(root):
        #     if not root:return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        return res