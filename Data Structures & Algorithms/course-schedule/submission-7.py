class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(c):
            if c in visited:
                return False
            if not hm[c]:
                return True
            visited.add(c)
            for r in hm[c]:
                res=dfs(r)
                if not res:
                    return False
            visited.remove(c)
            return True
        hm = {i:[] for i in range(numCourses)}
        for c,r in prerequisites:
            hm[c].append(r)
        visited = set()

        for c in hm:
            if not  dfs(c):
                return False
        return True


        