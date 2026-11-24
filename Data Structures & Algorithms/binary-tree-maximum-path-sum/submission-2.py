class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l_path = dfs(root.left)
            r_path = dfs(root.right)
            max_path = max(l_path, r_path)
            res = max(res, l_path + r_path + root.val, root.val)
            return max(root.val + max_path, root.val)  # returns the maximum 1d path

        return max(dfs(root), res)