class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache ={}
        def dfs(i,j,z):
            # case 1: all used up
            if i==len(s1) and j==len(s2) and z == len(s3):return True
            # if you finished using z at any time other than case 1
            if  z >= len(s3):return False
            if (i,j,z) in cache: return cache[(i,j,z)]
            # 1 used up but need to continue using others

            if i < len(s1) and s1[i] == s3[z] and dfs(i+1,j,z+1):return True
            if j < len(s2) and s2[j] == s3[z] and dfs(i,j+1,z+1):return True
            cache[(i,j,z)] = False
            return False
        return dfs(0,0,0)