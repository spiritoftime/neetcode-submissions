class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(l,r):
            # returns the indexes when it failed along with isPali
            while l <r:
                while l<r and not s[l].isalnum():l+=1
                while l<r and not s[r].isalnum():r-=1
                if s[l] != s[r]: return ((l,r),False)
                l+=1
                r-=1
            return ((0,0),True)
        indicies,isPalindrome = isPali(0,len(s) - 1)
        if not isPalindrome:
            l,r = indicies[0], indicies[1]
            return isPali(l+1,r)[1] or isPali(l,r-1)[1]
        else: return True
        
        