class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def backtrack(num_open,num_close,s):
            if num_open > n or num_close > n:
                return
            if num_close > num_open:
                return
            if num_open == n and num_close == n:
                self.res.append(s) 
            backtrack(num_open+1,num_close,s + "(")
            backtrack(num_open,num_close+1,s + ")")
        backtrack(1,0,"(")
        return self.res

                



        