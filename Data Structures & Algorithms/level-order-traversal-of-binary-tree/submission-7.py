# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        st = [root]
        res = []
        while st:
            level_len = len(st)
            level = []
            for i in range(level_len):
                n = st.pop(0)
                if n.left:
                    st.append(n.left)
                if n.right:
                    st.append(n.right)
                level.append(n.val)
            res.append(level)
        return res
            
