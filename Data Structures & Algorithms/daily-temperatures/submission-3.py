class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store (temperature, index)
        st=[]
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            # if incoming temperature is higher than previously encountered...
            while st and st[-1][0] < t:
                tmp, idx = st.pop()
                res[idx] = (i - idx)
            st.append([t,i])

        return res