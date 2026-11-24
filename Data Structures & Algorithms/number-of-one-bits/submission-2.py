class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            firstBitOn= n & 1
            if firstBitOn == 1:
                cnt+=1
            n = n>>1    
        return cnt