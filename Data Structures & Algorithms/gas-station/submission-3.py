class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        # guaranteed to have solution
        curr = 0
        feasible = 0
        for i in range(len(gas)):  
            curr += gas[i] - cost[i]
            if curr < 0: 
                feasible = i+1
                curr = 0
        return feasible