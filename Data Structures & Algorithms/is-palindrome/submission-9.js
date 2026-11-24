class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l =0
        let r = s.length -1
        while (l < r){
            const left = s[l]
            const right = s[r]
            if(!left.match(/^[a-zA-Z0-9]+$/) 
            ){
                l +=1
                continue
            }
            if(!right.match(/^[a-zA-Z0-9]+$/)) {
                r-=1
                continue
            }
            if(left.toLowerCase() !== right.toLowerCase()) return false
            l +=1
            r-=1
        }
        return true
    }
}
