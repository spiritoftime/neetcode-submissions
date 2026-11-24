class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hm = Counter(hand)
        for n in hand:
            if hm[n] == 0:continue # already used
            # make it the minimum first
            curr = n
            while curr -1 in hm and hm[curr-1] > 0:
                curr -=1
            # attempt to form a group of groupSize with the minimum
            for i in range(curr,curr+groupSize):
                # the nextnumber not inside or already used
                if i not in hm or hm[i] == 0:
                    return False
                hm[i] -=1
        return True