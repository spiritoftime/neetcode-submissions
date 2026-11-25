from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        numFresh = 0
        # when loop, add all the rotten and track number of fresh
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                f = grid[r][c]
                if f ==1:
                    numFresh += 1
                if f == 2:
                    q.append((r,c))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and numFresh > 0:
            n = len(q)
            for i in range(n):
                r,c = q.popleft()

                
                for x,y in directions:
                    if 0<=r+x<len(grid) and 0<=c+y<len(grid[0]) and grid[r+x][c+y] == 1:
                        grid[r+x][c+y] =2
                        numFresh -=1
                        q.append((r+x, c+y))
            time += 1
            
        return time if numFresh == 0 else -1