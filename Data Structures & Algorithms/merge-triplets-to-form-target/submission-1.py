class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def checkTriplets(t1):
            '''dont merge if any of them gives too much'''
            for i in range(len(t1)):
                if t1[i] > target[i]:
                    return False
            return True
        #2:01
        res = None
        for t in triplets:
            if t == target:return True
            if checkTriplets(t):
                if not res: res = t
                else:
                    res = [max(res[i],t[i]) for i in range(len(t))]
            if res == target:
                return True
        return res if res== target else False