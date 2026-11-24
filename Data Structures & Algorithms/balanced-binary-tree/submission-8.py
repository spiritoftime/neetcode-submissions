class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0, True]
            l_height, l_balanced = dfs(root.left)
            r_height, r_balanced = dfs(root.right)
            height = max(l_height, r_height) + 1
            return [height, l_balanced and r_balanced and abs(l_height - r_height) <= 1]

        return dfs(root)[1]
