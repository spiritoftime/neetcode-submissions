class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(c):
            if c in visiting:
                return False
            if c in added:
                return True
            visiting.add(c)
            for r in hm[c]:
                if not dfs(r):
                    return False
            res.append(c)
            visiting.remove(c)
            added.add(c)
            return True
        hm  = {i:[] for i in range(numCourses)}
        res = []
        visiting,added = set(),set()
        for c,r in prerequisites:
            hm[c].append(r)
        for c in hm:
            if not dfs(c):
                return []
        return res