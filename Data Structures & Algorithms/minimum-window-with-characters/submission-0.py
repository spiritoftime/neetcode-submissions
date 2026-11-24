class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c,0) + 1
        l,r= 0,0
        freq_curr = {}
        matches = len(freq_t)
        feasible_soln = None
        curr_matches = 0
        while r < len(s):
            curr = s[r]
            freq_curr[curr] = freq_curr.get(curr,0) + 1
            # it is one of the chars to match
            if curr in freq_t and freq_curr[curr] == freq_t[curr]:
                curr_matches += 1
            # if there is a complete match, should shrink the current window
            while curr_matches == matches:
                start = s[l]
                # current window will be the shortest substring
                if start in freq_t and freq_curr[start] - 1 < freq_t[start]:
                    # if there was a feasible soln and it has a shorter length
                    if not feasible_soln or (feasible_soln and r-l+1 < feasible_soln[1] - feasible_soln[0] + 1):
                        feasible_soln = (l,r)
                    curr_matches -=1
                    freq_curr[start] -=1
                    l+=1
                else: # shrink the window
                    freq_curr[start] -=1
                    l += 1
            r += 1
        return s[feasible_soln[0]:feasible_soln[1]+1] if feasible_soln else ""
