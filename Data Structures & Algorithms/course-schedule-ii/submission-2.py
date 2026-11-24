class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        added = set()
        def dfs(n):
            if n in added:
                return True
            if n in visit:
                return False
            visit.add(n)
            for pre in adj[n]:
                if not dfs(pre):
                    return False
            res.append(n)
            added.add(n)
            visit.remove(n)
            return True
        adj = {i:[] for i in range(numCourses)}
        for c,pre in prerequisites:
            adj[c].append(pre)
        res = []
        for c in adj:
            if not dfs(c):
                return []
        return res