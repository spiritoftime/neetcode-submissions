class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const hm = {}               // Frequency map of characters in the window
        let maxFreq = 0             // Most frequent character count in the window
        let l = 0                   // Left pointer of the sliding window
        let res = 0                 // Result: length of the longest valid window

        for (let e = 0; e < s.length; e++) {
            const c = s[e]
            hm[c] = (hm[c] ?? 0) + 1    // Update count of current char
            maxFreq = Math.max(maxFreq, hm[c])  // Track max frequency in window

            // If more than k replacements needed, shrink window from the left
            if ((e - l + 1) - maxFreq > k) {
                hm[s[l]] -= 1
                l += 1
            }

            res = Math.max(res, e - l + 1)   // Update max length
        }
        return res

    }
}
