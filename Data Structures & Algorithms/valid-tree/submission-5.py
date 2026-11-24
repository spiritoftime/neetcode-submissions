class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        def dfs(n, prev):
            if prevMap[n] and prevMap[n] != prev:
                return False
            if prevMap[n] and prevMap[n] == prev:
                return True
            prevMap[n] = prev
            for c in hm[n]:
                if c != prev: 
                    if not dfs(c, n):
                        return False
            return True
            
        prevMap = {i: False for i in range(n)}
        hm = {i: [] for i in range(n)}
        for e1, e2 in edges:
            hm[e1].append(e2)
            hm[e2].append(e1)
        
        if not dfs(0, 0):
            return False
        
        return all(prevMap[i] is not False for i in range(n))