class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hm = {}
        smallest = hand[0]
        # form freqMap
        for n in hand:
            hm[n] = hm.get(n,0) +1
        for n in hand:
            # go to the smallest (start) in the groupsize first!
            start = n
            while start-1 in hm and hm[start-1] > 0:
                start= start-1
            # Now, from that 'start', try to exhaust form groups starting from start
            while hm[start] > 0:
                for i in range(start, start + groupSize):
                    if hm.get(i, 0) <= 0:
                        return False
                    hm[i] -= 1
        return True

        
        

