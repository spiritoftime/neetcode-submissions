def isPalindrome( s: str) -> bool:
    l,r = 0,len(s)-1
    while l <r:
        while l <r and not s[l].isalnum():
            l+=1
        while l <r and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        def backtrack(combo,i):
            l,r = i,i+1
            if i == len(s):
                self.res.append(list(combo))
                return
            while l <r and r <= len(s):
                substr = s[l:r]
                if isPalindrome(substr):
                    combo.append(substr)
                    backtrack(combo, r)
                    combo.pop()

                r+=1
        backtrack([],0)
        return self.res