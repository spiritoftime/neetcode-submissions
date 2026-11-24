class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const res = []
        function backtrack(n, num_open, num_close, combo){
            if(num_open == n && num_close == n ) res.push(combo)

            if(num_open < n){
                backtrack(n,num_open + 1, num_close,combo + "(" )
            } if(num_close < num_open ){
                backtrack(n, num_open,num_close+1,combo+")")
            }
        }
        backtrack(n,0,0,"")
        return res
    }
}
