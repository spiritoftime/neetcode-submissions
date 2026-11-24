class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map,s2_map={},{}
        for i,c in enumerate(s1):
            s1_map[c] = s1_map.get(c,0) +1
        s2_map = {c:0 for c in s1_map}
        start = 0
        for i in range(len(s2)):
            c = s2[i]
            #if not relevant character, reset s2_map
            if c not in s2_map: 
                s2_map = {c:0 for c in s1_map}
                continue
            # it is a relevant character
            s2_map[c] +=1 
            # have we exceeded the number of chars for this specific char c?
            # if yes, we need to shrink the window, and then continue.
            while s2_map[c] > s1_map[c]:
                if s2[start] in s2_map: 
                    s2_map[s2[start]] -=1
                start +=1
            if s1_map == s2_map:return True
        return False
