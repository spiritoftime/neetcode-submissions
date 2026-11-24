
class Solution:
    def getFreqTup(self,t):
        s = "abcdefghijklmnopqrstupwxyz"
        ls_tup = [0 for i in range(26)]
        for c in t:
            ls_tup[s.index(c)] += 1
        return tuple(ls_tup)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            tup = self.getFreqTup(s)
            if tup in hm:
                hm[tup].append(s)
            else:
                hm[tup] = [s]
        return list(hm.values())



