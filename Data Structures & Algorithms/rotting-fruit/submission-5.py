from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs, get all rotten fruits then throw it to a queue, and track numfresh
        # use the length of q at the start to track mins
        q = deque()
        directions = [(0,1),(1,0), (-1,0), (0,-1)]
        fresh = 0
        mins = 0
        rows,cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == 2:
                    q.append((i,j))
                if cell == 1:
                    fresh += 1
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for i,j in directions:
                    new_r,new_c = r+i, c+j
                    if 0<=new_r<rows and 0<=new_c<cols and grid[new_r][new_c] ==1:
                        fresh -=1
                        grid[new_r][new_c] = 2
                        q.append((new_r,new_c))
            mins += 1
        return mins if fresh == 0 else -1


                    