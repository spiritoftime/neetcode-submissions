class Solution:
    def isValid(self, s: str) -> bool:
        hm = {"}":"{", ")":"(","]":"["}
        st = []
        i = 0
        while i < len(s):
            c = s[i]
            # close bracket found
            if c in hm:
                # no corresponding open bracket
                if not st or st[-1] != hm[c]: return False
                st.pop()
            #open bracket
            else:
                st.append(c)

            i+=1
        return len(st) ==0