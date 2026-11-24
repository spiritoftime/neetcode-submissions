# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack,curr,res = [],root,[]
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                if tmp.right:
                    curr = tmp.right
        return res[k-1]
            



        