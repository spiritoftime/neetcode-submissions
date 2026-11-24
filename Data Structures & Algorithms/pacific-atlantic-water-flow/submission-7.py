class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, ocean):
            if (i, j) in ocean:
                return
            """reverse water flow: normal water is 5->4. to reverse it it will be 5<-5 (or more)"""
            ocean.add((i, j))
            for x, y in directions:
                new_x, new_y = i + x, y + j
                if (
                    new_x < 0
                    or new_y < 0
                    or new_x >= len(heights)
                    or new_y >= len(heights[0])
                    or heights[new_x][new_y] < heights[i][j]
                ):
                    continue
                dfs(new_x, new_y, ocean)

        pac, at = set(), set()  # pac is top and left edges, at is right and btm edges
        for i in range(len(heights)):  # add the left and right
            dfs(i, 0, pac)
            dfs(i, len(heights[0]) - 1, at)

        for j in range(len(heights[0])):  # add the top and btm edges
            dfs(0, j, pac)
            dfs(len(heights) - 1, j, at)
        return list(pac & at)