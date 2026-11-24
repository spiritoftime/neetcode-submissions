from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque([])
        cLen = len(grid)
        rLen = len(grid[0])
        remaining = cLen * rLen
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                if curr == 0:
                    remaining -=1
                    visited.add((r,c))
                elif curr == 2:
                    q.append((r,c))
                    visited.add((r,c))
        res = 0
        while q:
            qLen = len(q)
            for i in range(len(q)):
                r,c = q.popleft()
                remaining -=1
                for r1,c1 in d:
                    newR = r+r1
                    newC = c+c1
                    if newR <0 or newC < 0 or newR>= len(grid) or newC >= len(grid[0]) or (newR,newC) in visited:
                        continue
                    q.append((newR,newC))
                    visited.add((newR,newC))
            if q: # check that it infected something during this second.
                res += 1
        if remaining > 0:
            return -1
        return res
