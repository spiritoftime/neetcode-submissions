# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(root,l_bound,r_bound):
            if not root:
                return True
            if not  l_bound<root.val < r_bound:
                return False
            return isValidNode(root.left, l_bound,root.val) and isValidNode(root.right,root.val,r_bound)
        return isValidNode(root,float('-inf'),float('inf'))


        