class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position desc
        combined = sorted(zip(position,speed),key=lambda x:x[0], reverse=True)
        # [(7,1),(4,2),(1,2),(0,1)]

        st = []
        for p,s in combined:
            time_needed = (target - p) / s
            # it is a slower fleet, so will make new fleet as no bottleneck.
            if st and time_needed > st[-1]:
                st.append(time_needed)
            if not st: st.append(time_needed)
        return len(st)