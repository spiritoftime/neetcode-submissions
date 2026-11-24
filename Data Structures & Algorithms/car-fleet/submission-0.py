class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        bottleneck = float('-inf')
        fleets = 0
        ps_sort= sorted(zip(position,speed),reverse=True,key=lambda x:x[0])
        print(ps_sort)
        for p,s in ps_sort:
            currTime = (target - p) / s
            if currTime > bottleneck:
                fleets += 1
                bottleneck = currTime
        return fleets
        