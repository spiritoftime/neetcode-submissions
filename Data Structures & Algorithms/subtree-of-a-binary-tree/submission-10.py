# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        # need this so that wont run into null pointer 
        # error when doing root.right/root.left at isSubtree
        if not root:
            return False
        # check is same at current root
        if isSame(root,subRoot):
            return True
        # check if any of the child nodes match subroot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)