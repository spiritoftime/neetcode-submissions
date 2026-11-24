class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0,0
        # expand until find substring that fufill all criteria, then shrink
        # until dont meet the criteria anymore. then continue expanding again
        # to find a new possible solution
        # critieria means to have all letters, AND in the frequency required per letter
        t_hm = {}
        currLen = float('inf')
        res = ""
        for c in t:
            t_hm[c] = t_hm.get(c,0) + 1
        curr_hm = {c:0 for c in t_hm}
        have,need = 0, len(t_hm)
        while end < len(s):
            curr = s[end]
            if curr in curr_hm:
                curr_hm[curr] += 1
                if curr_hm[curr] == t_hm[curr]: # just fufilled condition
                    have += 1
                while have == need: # attempt to shrink the window
                    start_char = s[start]
                    if start_char in curr_hm: #it is a valid letter
                        curr_hm[start_char] -=1
                        if curr_hm[start_char] < t_hm[start_char]: # do not fufill condition anymore
                            have -=1 
                    # include current solution as a possible solution first
                    if end - start + 1 < currLen: # new shortest solution
                        currLen = end-start+1
                        res = s[start:end+1]
                    start += 1 # always shrink the range
            end += 1
        return res