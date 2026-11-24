class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        t_map = ["+","-","*","/"]
        for t in tokens:
            if t in t_map:
                r=st.pop()
                l=st.pop()
                if t == "+":
                    res = l+r
                elif t =="-":
                    res = l-r
                elif t =="*":
                    res = l*r
                else:
                    res = int(l/r)
                st.append(res)
            else:st.append(int(t))
        return st[-1]