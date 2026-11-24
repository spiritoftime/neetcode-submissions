# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder,inorder):
            if not preorder or not inorder:return
            root = TreeNode(preorder[0])
            in_idx = inorder.index(preorder[0])
            root.left = dfs(preorder[1:], inorder[:in_idx])
            root.right = dfs(preorder[in_idx+1:], inorder[in_idx+1:])
            return root
        return dfs(preorder,inorder)