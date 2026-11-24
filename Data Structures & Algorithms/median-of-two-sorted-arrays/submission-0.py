class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #5:43
        A,B = nums1,nums2 # A will always be the smaller length array
        if len(nums2) < len(nums1):
            A,B = B,A
        half = (len(A) + len(B)) // 2
        l,r = 0,len(A)-1
        while True:
            mA = (l+r)//2
            mB = half - mA - 2
            lA,lB = float('-inf'),float('-inf')
            rA,rB = float('inf'),float('inf')
            if mA < len(A) and mA >=0: lA = A[mA]
            if mB < len(B) and mB >=0: lB = B[mB]
            if  mA+1 < len(A): rA = A[mA+1]
            if mB+1 < len(B): rB = B[mB+1]
            if lA > rB: 
                r = mA-1 # take less numbers here
                continue
            if lB > rA:
                l = mA+1 # take more at A
                continue
            if (len(A)+ len(B)) % 2 == 0: # even total length, middle
                return (max(lA,lB) + min(rA,rB)) /2
            else:return min(rA,rB)