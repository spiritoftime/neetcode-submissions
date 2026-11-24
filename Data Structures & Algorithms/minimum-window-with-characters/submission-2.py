class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep expanding window until you get all the letters
        # then, try to shrink it down to get the smallest window
        # (while all letters inside keep trying to shrink)
        # then continue trying to expand
        l,r, have = 0,0,0
        res = ""
        min_length = float('inf')
        curr_hm = {}
        t_hm = {}
        for c in t:
            t_hm[c] = t_hm.get(c,0) + 1
        need = len(t_hm)

        while r < len(s):
            c = s[r]
            if c in t_hm:
                curr_hm[c] = curr_hm.get(c,0) + 1
                if curr_hm[c] == t_hm[c]:
                    have += 1
            # shrink window while have all letters
            while need == have:
                if (r-l+1) < min_length:
                    res = s[l:r+1]
                    min_length = (r-l+1)
                if s[l] in curr_hm:
                    curr_hm[s[l]] -=1
                    if curr_hm[s[l]] < t_hm[s[l]]:
                        have -=1
                l+=1

            r+=1
        return res

        