class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for every temperature, store (temp, index) at stack.
        # if st not empty, should compare incoming (temp,index) with the top
        # while temp is more than the top, pop the top.
        # compute the number of days and put on res
        # finally append incoming (temp,index) to the stack.
        # at the end of the loop, should do a while loop.
        # set all temperatures still in index to 0 (no day.)
        st = []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            if not st:
                st.append((t,i))
            else:
                while st and st[-1][0] < t:
                    (existing_t, existing_i) = st.pop()
                    res[existing_i] = i - existing_i
                st.append((t,i))
        return res

        