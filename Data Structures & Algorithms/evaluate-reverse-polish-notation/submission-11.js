class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        for(const t of tokens){
            if(!isNaN(t)){
                stack.push(Number(t))
            }
            else{
                const r = stack.pop()
                const l = stack.pop()
                let total = 0
                if(t === "+"){
                    total = r+l
                }
                else if (t === "/"){
                    total = Math.trunc(l/r)
                }else if(t === "*"){
                    total = l * r
                }
                else{
                    total = l -r
                }
                stack.push(total)
            }
            
        }return stack[stack.length-1]
    }
}
