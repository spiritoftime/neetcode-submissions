class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        const q = [];
        const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        const rows = grid.length;
        const cols = grid[0].length;

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (grid[r][c] === 0) {
                    q.push([r, c]);
                }
            }
        }
        while(q.length > 0){
            const [r,c] = q.shift()
            for(const [r1,c1] of directions){
                const [newR,newC] = [r+r1,c+c1]
                    if(newR >= 0 && newC >= 0 && newR < grid.length
                    && newC < grid[0].length &&
                    grid[newR][newC] ==2147483647 ) {
                        grid[newR][newC] = grid[r][c] + 1
                        q.push([newR,newC])
                    }

            }
        }
     

        return grid;
    }
}
