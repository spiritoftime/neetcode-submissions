from string import ascii_lowercase
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lowers = ascii_lowercase
        hm = {
            2:lowers[0:3],
            3:lowers[3:6],
            4:lowers[6:9],
            5:lowers[9:12],
            6:lowers[12:15],
            7:lowers[15:19],
            8:lowers[19:22],
            9:lowers[22:26]
        }
        self.res = []
        def backtrack(i,combo):
            if i >= len(digits):
                self.res.append(''.join(combo))
                return
            currDigit = int(digits[i])
            if currDigit in hm:
                for s in hm[currDigit]:
                    combo.append(s)
                    backtrack(i+1,combo)
                    combo.pop()
            else:
                return
        if digits:
            backtrack(0,[])
        return self.res


        