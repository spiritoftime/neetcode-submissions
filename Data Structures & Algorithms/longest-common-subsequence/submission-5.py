class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0] * (len(text2))
        
        for c1 in text1:
            curr = [0] * len(text2)
            for i in range(len(text2)):
                if c1 == text2[i]:
                    curr[i] = (prev[i-1] if i > 0 else 0) + 1
                else:
                    curr[i] = max(prev[i], curr[i-1] if i > 0 else 0)
            prev = curr
        
        return prev[-1]