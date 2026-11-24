# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            i_in = inorder.index(preorder[0])
            root.left = dfs(preorder[1:i_in+1], inorder[:i_in])
            root.right = dfs(preorder[i_in+1:], inorder[i_in+1:])
            return root
        return dfs(preorder,inorder)

            