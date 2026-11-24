class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort the hand
        # from the largest number, try to keep getting largest - 1 until groupsize.
        # any time this is not true -> false
        # repeat until no more cards.
        hm = {}
        for n in hand:
            hm[n] = hm.get(n,0) +1
        remaining = len(hand)
        while remaining > 0:
            largestNumber = max(item[0] for item in hm.items() if item[1] > 0)
            for i in range(largestNumber,largestNumber-groupSize,-1):
                if i not in hm or hm[i] == 0:
                    return False
                hm[i] -=1
                remaining -=1
        return True