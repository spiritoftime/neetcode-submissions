class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        const directions = [[1,0],[0,1],[-1,0],[0,-1]]
        const q = []
        let fresh = 0
        for (let i = 0 ; i < grid.length; i ++){
            for (let j = 0 ; j < grid[0].length; j ++){
                if(grid[i][j] === 2){
                    q.push([i,j])
                }
                if(grid[i][j] == 1){
                    fresh +=1
                }
            }
        }
        let mins = 0
        while(q.length > 0 && fresh > 0){
            const qLen = q.length

            for(let i = 0; i < qLen; i ++){
                const [l,r] = q.shift()

                for(const [l1,r1] of directions){
                    const [newL,newR] = [l+l1,r+r1]
                    if(newL >=0 && newR >=0 && newL < grid.length
                    && newR < grid[0].length && grid[newL][newR] ==1 ){
                        q.push([newL,newR])
                        grid[newL][newR] = 2
                        fresh -=1
                    }
                }
            }
          
            mins++
        }
        return fresh === 0 ?mins : -1
    }
}
