# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        bfs = deque()
        bfs.append(root)
        res = []
        while bfs:
            curr = []
            for i in range(len(bfs)):
                n = bfs.popleft()
                if n.left:
                    bfs.append(n.left)
                if n.right:
                    bfs.append(n.right)
                curr.append(n.val)
            res.append(list(curr))
        return res
