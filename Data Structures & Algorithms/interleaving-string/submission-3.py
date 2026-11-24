from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ''' at every character, you can choose to use s1 or s2. if cannot use
        either it cannot be interwoven'''
        @lru_cache()
        def dp(i,j):
            if i+j == len(s3):
                # reached end of s3
                return  i==len(s1) and j == len(s2) 
            if i < len(s1) and s1[i] == s3[i+j]:
                if dp(i+1,j): return True
            if j < len(s2) and s2[j] == s3[i+j]:
                if dp(i,j+1): return True           

            return False
        return dp(0,0)