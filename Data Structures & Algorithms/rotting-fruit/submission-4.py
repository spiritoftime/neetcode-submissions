class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        visited = set()
        to_infect = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == 2:
                    queue.append((i, j))
                if curr == 1:  # fresh
                    to_infect += 1
        time_taken = 0
        while queue:
            iterations = len(queue)
            for n in range(iterations):
                (i, j) = queue.pop(0)
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1:
                    to_infect -= 1
                visited.add((i, j))
                grid[i][j] = 2
                for x, y in directions:
                    new_x = i + x
                    new_y = y + j
                    if (
                        new_x < 0
                        or new_x >= len(grid)
                        or new_y < 0
                        or new_y >= len(grid[0])
                    ):
                        continue
                    if grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
            if queue:
                time_taken += 1
        return time_taken if to_infect == 0 else -1       