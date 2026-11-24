# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ls = []
        st = [root]
        while st:
            level = len(st)
            levelList = []
            for i in range(level):
                n = st.pop(0)
                levelList.append(n.val)
                if n.left:
                    st.append(n.left)
                if n.right:
                    st.append(n.right)
            ls.append(levelList)
        return ls
                

