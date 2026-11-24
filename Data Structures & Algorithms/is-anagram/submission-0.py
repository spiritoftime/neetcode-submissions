class Solution:
    def countChars(s):
        s_hashmap = {}
        for c in s:
            if c not in s_hashmap:
                s_hashmap[c] = 1
            else:
                s_hashmap[c] += 1
        return s_hashmap
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Solution.countChars(s)
        t_map = Solution.countChars(t)
        return s_map == t_map

        
        