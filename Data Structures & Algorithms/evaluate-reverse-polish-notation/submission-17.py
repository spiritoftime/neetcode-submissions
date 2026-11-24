class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        st = []
        for t in tokens:
            if t in operators:
                r,l = st.pop(), st.pop()
                res=0
                if t == "+":
                    res = l+r
                elif t == "*":
                    res = l*r
                elif t == '-':
                    res = l - r
                else:
                    res = int(l/r) # dont use //
                st.append(res)
            else:
                st.append(int(t))
        return st[-1]