class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let l = 0
        let maxLen = 0
        const hm = {}
        let res = 0
        for (let j = 0; j < s.length; j ++){
            const c = s[j]
            hm[c] = (hm[c] ?? 0) + 1
            maxLen = Math.max(hm[c], maxLen)
            if((j -l+1) - maxLen > k){
                hm[s[l]] -= 1
                l+=1
            }
            res = Math.max(
                j-l+1,
            res
            )
        }
        return res
    }
}
