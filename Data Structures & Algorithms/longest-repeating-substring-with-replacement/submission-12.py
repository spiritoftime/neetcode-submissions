class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            hm[c] = hm.get(c,0) + 1
            # still enough replacements
            if max(hm.values()) + k >= i - start + 1:
                res = max(res, i - start + 1)
            else:
                # shrink the window
                while max(hm.values()) + k < i - start + 1:
                    start_c = s[start]
                    hm[start_c] -=1
                    start += 1
        return res

