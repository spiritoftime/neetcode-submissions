class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        // RPN : whenever operator encountered pop the last 2 numbers
        function performOperation(l,r,op){
            if(op === "+"){
                return l + r
            } else if (op === "-"){
                return l - r

            } else if (op === "/"){
                return Math.trunc(l /r)
            }
             return l * r
        }
        const stack = []
        let total = 0

        for(const t of tokens){
            // it is a number
            if(!isNaN(t)){
                stack.push(parseFloat(t))
            }
            else{
                const r = stack.pop()
                const l = stack.pop()
                total = performOperation(l,r,t)
                // put back total
                stack.push(total)
            }
        }
        return stack.pop();
        
    }
}
