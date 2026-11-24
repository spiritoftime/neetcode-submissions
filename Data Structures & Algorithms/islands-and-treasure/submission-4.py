from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque([])
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))

        while q:
            r,c,area = q.popleft()
            if grid[r][c] >0:
                grid[r][c] = area
            for r1,c1 in d:
                newR = r+r1
                newC = c+c1
                if newR <0 or newC <0 or newR>=len(grid) or newC>=len(grid[0]) or grid[newR][newC] < 0 or (newR,newC) in visited:
                    continue
                q.append((newR,newC,area + 1))

                visited.add((newR,newC))
    
                