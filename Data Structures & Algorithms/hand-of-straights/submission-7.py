class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hm = Counter(hand)
        for n in hand:
            if hm[n] == 0: continue # used
            # get the start number (the smallest)
            start=n
            while start -1 in hm and hm[start-1]>0:
                start -=1
            for i in range(start, groupSize+start):
                # used up
                if hm[i] <=0: return False
                hm[i]-=1
        return True