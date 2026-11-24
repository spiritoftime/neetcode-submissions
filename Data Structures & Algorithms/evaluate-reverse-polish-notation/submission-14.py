class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # append the numbers to a stack.
        # if encounter a operation, should remove top 2 elements and recompute
        # then push back the computed result to the stack.
        operations = ['*','+','-','/']
        st = []
        for t in tokens:
            if t not in operations: # a number
                st.append(int(t))
            else:
                r = st.pop()
                l = st.pop()
                # r,l = st.pop(),st.pop()
                res = 0
                if t == '*':
                    res = l * r
                elif t == '/':
                    res = int(l / r)
                elif t == '+':
                    res = l + r
                else:
                    res = l-r
                st.append(res)
        return st[-1]
        