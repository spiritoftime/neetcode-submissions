class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # Convert list to tuple
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        return list(hm.values())