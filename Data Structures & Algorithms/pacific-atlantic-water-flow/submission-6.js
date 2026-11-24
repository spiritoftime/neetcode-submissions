class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {
        const ROWS = heights.length
        const COLS = heights[0].length
        const directions = [[0,1], [1,0], [ -1,0], [0,-1]]
        function dfs(ocean,r,c){
            if(ocean[r][c]) return
            ocean[r][c] = true
            for(const [r1,c1] of directions){
                const newR = r1+r
                const newC = c1+c
                
                if(newR <ROWS && newC < COLS && newR>=0 && newC >=0 &&
                heights[newR][newC] >= heights[r][c]) {
                    dfs(ocean,newR,newC)
                }

            }
        }
        const res = []
        const pac = Array.from({length:ROWS},()=>Array.from({length:COLS}))
        const atl = Array.from({length:ROWS},()=>Array.from({length:COLS}))
        for(let i =0 ; i < ROWS; i ++){
            dfs(pac,i,0)
            dfs(atl,i,heights[0].length - 1)
        }
        for(let c =0; c < COLS; c++){
            dfs(pac,0,c)
            dfs(atl,heights.length - 1, c)
        }
        for(let i =0 ; i < ROWS; i ++){
            for(let c =0; c < COLS; c++){
                if(pac[i][c] && atl[i][c]) res.push([i,c])
            }
        }
        return res
    }
}
