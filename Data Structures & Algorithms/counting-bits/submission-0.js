class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    convertToBinary(n){
        // get the bit out
        let res=0
        while (n > 0){
            if (n %2 == 1){
                res +=1

            }
            n = n >> 1

        }
        return res
    }
    countBits(n) {
        const res = []
        let binary = 0;
        for(let i = 0; i <= n; i ++){
            binary = this.convertToBinary(i)
            res.push(binary)
            
        }
        return res
    }
}
