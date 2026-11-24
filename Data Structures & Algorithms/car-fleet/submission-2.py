class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by (pos,speed) via descending pos
        # put to a stack
        # loop through it and always compare with the stack, if have a finish time
        # more than the top, then append to stack.
        info = sorted(zip(position, speed), reverse=True)
        st = []
        for pos, sp in info:
            tt = (target - pos) / sp
            if st and st[-1] < tt: # the incoming fleet is slower than the most recent car
                st.append(tt)
            elif not st:
                st.append(tt)
        return len(st)