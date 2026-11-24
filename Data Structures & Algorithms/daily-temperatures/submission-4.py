class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # next greater
        res = [0] * len(temperatures)
        #store the index of the temperatures
        st = []
        for i,t in enumerate(temperatures):
            # if there is a greater element found, pop from stack and append the result.
            while st and temperatures[st[-1]] < t:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
            # at the end, the st will still have items (those with no greater elements). however, we alr set default res to 0
        return res

