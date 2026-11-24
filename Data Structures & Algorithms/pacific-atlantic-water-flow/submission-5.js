class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {
        const ROWS = heights.length
        const COLS = heights[0].length
        const directions = [[1,0],[-1,0],[0,1],[0,-1]]
        let pac = Array.from({ length: ROWS }, () => 
                  Array(COLS).fill(false));
        let atl = Array.from({ length: ROWS }, () => 
                  Array(COLS).fill(false));    
        const dfs = (ocean,r,c)=>{
            if(ocean[r][c]) return
            ocean[r][c] = true
            for(const [r1,c1] of directions){
                const newR = r+r1
                const newC = c1+c
                if(newR >=0 && newC >=0 && newR < ROWS && newC < COLS
                && heights[newR][newC] >= heights[r][c]){
                    dfs(ocean,r+r1,c+c1)
                }
            }
        }
        for (let c = 0; c < COLS; c++) {
            dfs(pac, 0, c);
            dfs(atl, ROWS - 1, c);
        }
        for (let r = 0; r < ROWS; r++) {
            dfs(pac, r, 0);
            dfs(atl, r, COLS - 1);
        }
        let res = []
        for(let r = 0; r < ROWS; r++){
            for(let c = 0; c<COLS; c++){
                if(pac[r][c] && atl[r][c]){
                    res.push([r,c])
                }
            }
        }
        return res
}
}