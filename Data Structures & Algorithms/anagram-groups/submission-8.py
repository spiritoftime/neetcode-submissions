
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            # append -> None so use this
            hm[sorted_s] = hm.get(sorted_s, []) + [s]
        return list(hm.values())