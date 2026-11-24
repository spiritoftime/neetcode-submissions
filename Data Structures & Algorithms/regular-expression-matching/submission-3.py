class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i >=len(s) and j>=len(p):return True
            # pattern used up but dont fully match
            if j >= len(p): return False
            # dont check i >= len(s) return False!
            # eg. s=aa, p = a*a -> True
            match = (i < len(s)) and (p[j] == "." or s[i] == p[j])
            if j +1 < len(p) and p[j+1] == "*":
                # you can use curr 0 times -> 1 extra chance when dont match
                # s=a,p=c*a, dont use c at all!
                skip_curr = dfs(i,j+2)
                # reuse the curr multiple times.
                repeat_curr = match and dfs(i+1,j)
                cache[(i,j)] = skip_curr or repeat_curr 
            else:
                if match:
                    cache[(i,j)] = dfs(i+1,j+1)
                else: cache[(i,j)] =False
            return cache[(i,j)] 
        return dfs(0,0)
