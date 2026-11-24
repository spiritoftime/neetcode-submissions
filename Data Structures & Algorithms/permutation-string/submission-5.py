from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {c:0 for c in s1_map}
        l=0
        for i in range(len(s2)):
            c = s2[i]
            if c in s1_map:
                s2_map[c]+=1
                # ccab vs cab in s1
                while s2_map[c]> s1_map[c]:
                    s2_map[s2[l]] -=1
                    l+=1
                if s1_map == s2_map: return True
            else:
                s2_map = {c:0 for c in s1_map}
                l = i+1

        return False