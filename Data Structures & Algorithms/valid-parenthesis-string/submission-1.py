class Solution:
    def checkValidString(self, s: str) -> bool:
        '''store the indexes of open_st and chances (*)'''
        open_st = []
        chances = []
        r = 0
        while r < len(s):
            curr = s[r]
            if curr == '(':
                open_st.append(r)
            elif curr=='*':
                chances.append(r)
            else: # close bracket
                if open_st: # there is a corresponding open bracket
                    open_st.pop()
                elif chances: chances.pop()
                else: return False
            r+=1
        while open_st:
            if not chances or chances[-1] < open_st[-1]: return False
            open_st.pop()
            chances.pop()
        return True