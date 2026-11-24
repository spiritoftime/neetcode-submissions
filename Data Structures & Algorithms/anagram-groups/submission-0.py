class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hm = {}
        for s in strs:
            s_tup = tuple(c for c in sorted(s))
            if s_tup in hm:
                hm[s_tup].append(s)
            else:
                hm[s_tup] = [s]
        for v in hm.values():
            output.append(v)
        return output

