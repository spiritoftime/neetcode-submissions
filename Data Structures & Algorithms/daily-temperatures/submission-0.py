class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            # check if there is a top and if the top temp is lower than t.
            if not stack:
                stack.append((i,t))
            else:
                while stack and stack[-1][1] < t:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i,t))
        return res
        