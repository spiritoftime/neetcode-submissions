# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,isBalanced): 
            if not root:return 0,True
            l,lBalanced = dfs(root.left,isBalanced)
            r,rBalanced=dfs(root.right,isBalanced)
            # doesnt matter what height you return, need return something so that can get False when not balanced
            if abs(l-r) >1 or not lBalanced or not rBalanced:return 0,False
            return max(l,r)+1,True
        return dfs(root,True)[1]
