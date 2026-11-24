class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []
        const hm = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for(const c of s){
            // opening bracket
            if(!(c in hm)){
                stack.push(c)
            }
            else{
                if(stack.length == 0 || stack[stack.length - 1 ] != hm[c]){
                    return false
                }
                stack.pop()
            }
        }
        return stack.length === 0 
    }
}
