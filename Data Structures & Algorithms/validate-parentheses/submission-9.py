class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close_open = {"}":"{", ")":"(", "]":"["}
        for c in s:
            if c not in close_open: # it is open bracket
                st.append(c)
            else:
                if not st or st[-1] != close_open[c]: # dont have opening bracket
                    return False
                st.pop()
        return len(st) == 0 # fully closed