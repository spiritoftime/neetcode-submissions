# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = []
        curr = root
        prev = root
        res = []

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            tmp = st[-1] # explore it
            if tmp.right:
                if prev == tmp.right:
                    tmp = st.pop()
                    res.append(tmp.val)
                    prev = tmp
                    continue
                 # need to prevent infinite loop here.
                curr = tmp.right
            else:
                tmp = st.pop() # only pop 
                res.append(tmp.val)
                prev = tmp
        return res
