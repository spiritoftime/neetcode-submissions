class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        state = []
        def backtrack(s):
            if not s and len(state) == 4: # reached the end and only 4 parts
                res.append(".".join(state))
                return
            if not s or len(state) == 4: return # not valid IP anymore
            if s[0] == "0": # only can explore one possible state, since leading zero
                state.append("0")
                backtrack(s[1:])
                state.pop()
            else:
                # if you do for i in range(1,4) you have duplicate solutions
                # try to take from 1 to the last letter
                # you do len(s) + 1 because in slicing, end index needs to be +1.
                for i in range(1,min(4, len(s) +1)):
                    curr = s[:i]
                    if int(curr) <= 255:
                        state.append(curr)
                        backtrack(s[i:])
                        state.pop()
        backtrack(s)
        return res