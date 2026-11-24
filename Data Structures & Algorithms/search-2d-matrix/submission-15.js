class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    binarySearchColumn(matrix, target,col){
        let l = 0
        let r = matrix[col].length -1
        while (l <=r){
            const m = Math.floor((l+r) /2)
            if(matrix[col][m] == target) return true
            if(matrix[col][m] > target){
                r = m-1
            }
            else{
                l = m+1
            }

        }
        return false

    }
    searchMatrix(matrix, target) {
        for(let i = 0 ; i < matrix.length ; i ++){
            const l = matrix[i][0]
            const r = matrix[i][matrix[i].length - 1]
            if( target >= l && target <= r){
                return this.binarySearchColumn(matrix,target,i)
            }
        }
        return false
    }
}
