class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close_open = {'}':'{',']':'[',')':'('}
        for c in s:
            if c not in close_open: #it is an open bracket
                st.append(c)
            else:
                if not st: # no more open brackets to close
                    return False
                top = st[-1]
                if st[-1] != close_open[c]:
                    return False
                # open bracket closed, pop
                st.pop()
        # there should not be any open brackets
        return True if not st else False 

        