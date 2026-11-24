class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # only when the grids are submerged can you start to swim
        # this is basically dijkstra's algorithm, min cost to reach end
        considerations = [(grid[0][0],0,0)] # (height needed, i,j)
        visited = set()
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        while considerations:
            t, i,j = heapq.heappop(considerations)
            if (i,j) in visited: continue
            visited.add((i,j))
            # need to add cost to reach the bottom too, so must be after the cost
            if i == len(grid)-1 and j == len(grid[0]) -1: return t

            for r,c in directions:
                new_i = i + r
                new_j = j + c
                if new_i <0 or new_j <0 or new_i >= len(grid) or new_j >= len(grid[0]) or (new_i,new_j) in visited: continue # out of bounds
                heapq.heappush(considerations,(max(t,grid[new_i][new_j]), new_i, new_j))

