# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, prev):
            # if they are in same side, need to go down
            if p.val < root.val and q.val < root.val:return dfs(root.left,root)
            elif p.val > root.val and q.val >root.val:return dfs(root.right,root)
            # if they are in diff sides of root -> root is LCA
            elif p.val < root.val <q.val or q.val < root.val <p.val:return root,root
            else: # one of them is the LCA
                if root.val == p.val: return p, root
                return q, root
        return dfs(root,root)[0]