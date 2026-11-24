class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        queue = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == 0:  # water
                    queue.append((i, j))
        distance = 0
        while queue:
            depth_iterations = len(queue)
            for n in range(depth_iterations):
                (i, j) = queue.pop(0)
                if (i, j) in visited:
                    continue
                grid[i][j] = min(grid[i][j], distance)
                visited.add((i, j))
                for x, y in directions:
                    new_x = i + x
                    new_y = j + y
                    if (
                        new_x < 0
                        or new_y < 0
                        or new_x >= len(grid)
                        or new_y >= len(grid[0])
                    ):
                        continue
                    if grid[new_x][new_y] != 0 and grid[new_x][new_y] != -1:
                        queue.append((new_x, new_y))
            distance += 1
