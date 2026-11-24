class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        function dfs(r,c,curr){
            if (r <0 || c < 0 || r == grid.length || c == grid[0].length) return 0
            if(grid[r][c] == 0) return 0
            grid[r][c] = 0
            return 1+ dfs(r,c+1) + dfs(r +1,c) + dfs(r, c-1) + dfs(r-1,c) 

        }
        let res = 0
        for (let r = 0; r < grid.length ; r ++){
            for (let c = 0; c < grid[0].length; c ++){
                if(grid[r][c]==1)
                {
                    res = Math.max(dfs(r,c), res)
                }
            }
        }
        return res
    }
}
