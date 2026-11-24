class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map,t_map = {},{}

        start = 0
        res = ""
        curLen = float('inf')
        for i in range(len(t)):
            c = t[i]
            t_map[c] = t_map.get(c,0) +1
        s_map = {c:0 for c in t_map}

        want = len(t_map.keys())
        have = 0


        for i in range(len(s)):
            # expand window until we get all characters in the substring
            c = s[i]
            if c in s_map: 
                s_map[c] += 1
                if s_map[c] == t_map[c]: have +=1
            #possible valid soln

            while want == have:
                end = i
                if end - start +1 < curLen:
                    res = s[start:end+1]       
                    curLen = end- start +1
                # start to shrink the window
                if s[start] in s_map:
                    s_map[s[start]] -=1
                    if s_map[s[start]] < t_map[s[start]]: 
                        have -=1

                start +=1
    
        return res

