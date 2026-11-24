# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root,p,q):

            if p.val < root.val and q.val < root.val:
                return dfs(root.left, p,q)
            if p.val > root.val and q.val > root.val:
                return dfs(root.right, p,q)
            # if they both diverge (eg. p less than root and q more than root or vice
            # versa, then it is the lowest common ancestor)
            return root
        return dfs(root,p,q)