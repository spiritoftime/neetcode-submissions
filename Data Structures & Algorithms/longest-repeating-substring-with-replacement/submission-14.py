class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        left = 0
        for i in range(len(s)):
            c = s[i]

            hm[c] = hm.get(c,0) + 1
            # more than k replacements, need to start shrinking
            while (i-left+1) - max(hm.values()) > k:
                hm[s[left]] -=1
                left += 1

            res = max(res, i - left +1)

        return res

