# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st,res = [],[]
        curr = root
        prev = root
        while st or curr:
            while curr is not None:
                st.append(curr)
                curr = curr.left
            tmp = st[-1]
            if tmp.right is not None:
                if tmp.right == prev:
                    st.pop()
                    prev= tmp
                    res.append(tmp.val)                    
                else:
                    curr = tmp.right
            else:
                st.pop()
                prev= tmp
                res.append(tmp.val)
        return res