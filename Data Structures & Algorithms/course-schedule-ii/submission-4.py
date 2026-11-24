class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        def detectCycle(c, completed,visiting, res, adjList):
            if c in completed:return False 
            if c in visiting:return True
            visiting.add(c)
            for neigh in adjList[c]:
                if detectCycle(neigh, completed,visiting,res,adjList):return True
            completed.add(c)
            visiting.remove(c)
            res.append(c)
            return False

        adjList={n:[] for n in range(numCourses)}
        for c, pre in prerequisites:
            adjList[c].append(pre)
        visiting,completed=set(),set()
        for c in adjList:
            if detectCycle(c,completed,visiting,res, adjList):
                return []
        return res































