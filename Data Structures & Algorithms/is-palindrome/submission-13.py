class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            l_c = s[l].lower()
            r_c = s[r].lower()
            if l_c != r_c:
                return False
            l +=1
            r-=1
        return True
        #9ababa
        