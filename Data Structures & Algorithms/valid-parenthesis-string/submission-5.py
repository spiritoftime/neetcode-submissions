class Solution:
    def checkValidString(self, s: str) -> bool:
        open,star =[],[]
        for i, c in enumerate(s):
            if c == "(":open.append(i)
            if c == "*":star.append(i)
            if c == ")":
                # no early star issue for ) -> star needs to be early to close )!
                if open: # can use this open
                    open.pop()
                else:
                    if star:star.pop() # use star
                    else:return False
        while open:
            # star appeared after open 
            # star cannot be used if appear before open
            # *( should be False
            if star and star[-1] > open[-1]: 
                star.pop()
                open.pop()
            else:return False
        return not open



        # *( should be False, but will return True here (star too early)
        hm = {"(":0, "*":0}
        for c in s:
            if c == ")":
                if hm["("] == 0 and hm["*"] == 0: return False # ")" came first
                if hm["("]>0:hm["("] -=1
                else:
                    if hm["*"]>0:hm["*"]-=1
            else:hm[c]+=1
        return hm["*"] >= hm["("]