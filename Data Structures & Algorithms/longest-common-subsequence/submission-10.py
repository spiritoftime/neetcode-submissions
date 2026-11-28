class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev=[0 for i in range(len(text2))]
        for c in text1:
            curr = [0 for i in range(len(text2))]
            # if match
            for i in range(len(curr)):
                if text2[i] == c:
                    curr[i] = (prev[i-1] if i >0 else 0) + 1
                else:
                    curr[i] = max(curr[i-1] if i >0 else 0, prev[i])
            prev=curr
        return prev[-1]