class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(c,visited):
            if c in visited:
                return False
            if not hm[c]:
                return True
            visited.add(c)
            for r in hm[c]:
                res=dfs(r,visited)
                if not res:
                    return False
            return True
        hm = {i:[] for i in range(numCourses)}
        for c,r in prerequisites:
            hm[c].append(r)
        for c in hm:
            visited = set()
            if not  dfs(c,visited):
                return False
        return True


        