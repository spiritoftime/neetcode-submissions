class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */

    countBits(n) {
        let offset = 1;
        const res = []
        // base case 0 has no 1s
        res.push(0)
        for(let i = 1; i < n +1; i++){
            // you only add 1 when it is a new significant bit - 2/4/8.
            // hence, offset keeps track of the most significant bit as we go along
            if (offset * 2 == i){
                offset = i
            }
            // dp: each result is the result of the number without the signficant bit
            res.push(1 + res[i - offset])

        }
        return res
    }
}