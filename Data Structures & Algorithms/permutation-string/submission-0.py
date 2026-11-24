from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        cnt_s1 = Counter(s1)
        hm = {c:0 for c in set(s1)}
        for i in range(len(s2)):
            c = s2[i]
            if c not in hm:
                hm = {c:0 for c in set(s1)}
                l = i+1
            else:
                hm[c] += 1
                if hm[c] > cnt_s1[c]:
                    hm[s2[l]] -=1
                    l +=1
                if hm == cnt_s1:return True
        return False

