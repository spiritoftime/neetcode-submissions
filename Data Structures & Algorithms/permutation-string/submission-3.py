from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation exists if we can find a substring with same chars and same freq
        s1_map = Counter(s1)
        cnt = {}
        for i in range(len(s2)):
            c = s2[i]
            if c not in s1_map: # invalid
                cnt = {}
            else:
                cnt[c] = cnt.get(c,0) + 1
                if cnt == s1_map: return True
                if cnt[c] > s1_map[c]: # shrink the window
                    start = i - sum(cnt.values()) + 1
                    while cnt[c] > s1_map[c]:
                        cnt[s2[start]] -=1
                        start += 1
        return False
