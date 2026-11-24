class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxLen = 0
        let l = 0
        const hm = {}
        for(let i = 0; i < s.length ; i ++){
            const c = s[i]
            hm[c] = (hm[c] ?? 0) + 1
            while(hm[c] > 1){
                hm[s[l]] -=1
                l +=1
            }
            maxLen = Math.max(maxLen, (i-l+1))
        }
        return maxLen
    }
}
