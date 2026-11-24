class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # candidates for merging are those with at least 1 val == target and
        # all vals must be less than the ones in target
        def validCandidate(t1):
            return ((t1[0]<= target[0] and t1[1] <= target[1] and t1[2] <= target[2]) and 
            (t1[0] == target[0] or t1[1]==target[1] or t1[2] == target[2]))
        def merge(t1,t2):
            return [max(t1[0],t2[0]),max(t1[1],t2[1]),max(t1[2],t2[2]) ]
        bfs = []
        for t in triplets:
            if validCandidate(t): bfs.append(t)
        while len(bfs) >= 2:
            t1,t2 = bfs.pop(), bfs.pop()
            merged = merge(t1,t2)
            bfs.append(merged)
        if not bfs:return False
        t1 = bfs.pop()
        return t1[0] == target[0] and t1[1]==target[1] and t1[2] == target[2]
            
