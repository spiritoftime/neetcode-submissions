# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def inorder(root,k):
            nonlocal cnt
            if not root:return
            n = inorder(root.left,k)
            if n:
                return n
            cnt += 1
            if cnt == k:
                return root
            return inorder(root.right,k)
        res= inorder(root,k)
        return res.val if res else None