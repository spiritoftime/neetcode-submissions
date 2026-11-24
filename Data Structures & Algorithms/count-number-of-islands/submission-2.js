class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        let res = 0
        function dfs(r,c){
            if(r == grid.length || r <0 || c == grid[0].length || c <0)return;
            if(grid[r][c] == "0") return
            grid[r][c] = "0"
            dfs(r +1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        }
        for(let r = 0;  r < grid.length; r++){
            for (let c =0; c<grid[0].length;c++){
                if(grid[r][c] == "1"){
                    res += 1
                    dfs(r,c)
                }

            }
        }
        return res
    }
}
