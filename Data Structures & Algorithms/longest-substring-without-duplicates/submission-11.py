class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_ls = []
        res =0
        for c in s:
            while c in substr_ls:
                substr_ls.pop(0)
            substr_ls.append(c)
            res = max(res,len(substr_ls))

        return res
