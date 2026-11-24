class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(n,prev):
            if n in visited:
                return False
            visited.add(n)
            for c in adj[n]:
                if c == prev: # prevent going back
                    continue
                if not dfs(c,n):
                    return False
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        return dfs(0, -1) and n == len(visited)
