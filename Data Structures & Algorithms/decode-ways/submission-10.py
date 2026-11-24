class Solution:
    def numDecodings(self, s: str) -> int:
        # at every stage, we can take 1 char or 2 char.
        # one just takes the curr char, two takes the previous char too
        # start with 1 
        one, two = 1,0
        for j in range(len(s) -1, -1, -1):
            tmp = one
            curr = s[j]
            if curr == "0":
                one = 0
            else:
                if  j +1 < len(s) and int(s[j:j+2]) <= 26: # you can take 2 letters
                    one = one + two
            two = tmp
        return one
            