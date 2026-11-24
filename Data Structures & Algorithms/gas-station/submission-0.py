class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def travel(i, curr, travelled):
            if travelled == len(gas):
                return (True,i)
            curr = curr + gas[i] # fill up first
            cost_needed = cost[i]
            if curr - cost_needed <0: # unable to proceed
                return (False,i)
            # cross and refill
            travelled += 1
            if i + 1 >= len(gas):
                return travel(0, curr - cost_needed,travelled)
            else:
                return travel(i+1, curr - cost_needed,travelled)
        feasible = 0
        while feasible < len(gas):
            res = travel(feasible,0,0)
            if not res[0]:
                # If we failed at a station before our starting point,
                # we've wrapped around - no solution exists
                if res[1] < feasible:
                    return -1
                feasible = res[1] + 1 # everything it has travelled not feasible
            else:
                return feasible
        return -1
        #         return i
        # return -1