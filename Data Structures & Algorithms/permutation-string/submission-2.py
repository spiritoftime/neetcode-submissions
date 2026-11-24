class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if we encounter a character not in s1, we should reset everything.
        # if there is more frequency then needed, should shrink the window.
        # how may i increment start? i should start only when it is a letter
        # inside s1, but shouldnt set it every time.
        freq_map = {c:0 for c in s1} 
        s1_map = {c:s1.count(c) for c in s1} # for comparison to see needed freq
        target = len(freq_map.keys())
        start = 0
        met_req = 0
        for i,c in enumerate(s2):
            if c not in freq_map:
                met_req = 0
                freq_map = {c:0 for c in s1}
                continue
            start = i - sum(freq_map.values())

            freq_map[c] += 1

            if freq_map[c] == s1_map[c]:
                met_req += 1
            while freq_map[c] > s1_map[c]:
                # previously met target need to decrement
                if freq_map[s2[start]] == s1_map[s2[start]]:
                    met_req -=1
                freq_map[s2[start]] -=1
                start +=1
            if met_req == target:
                return True
        return False