class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip the position and speed array into (p,s)
        # sort by descending order position
        # maintain a stack for time taken to reach destination. this stack
        # will be the number of car fleets.
        # loop through the zipped array. if time_taken <= the top of the stack,
        # dont add to stack as you cannot overtake.
        # if it takes longer than the stack, it is a slower car fleet, so can
        # add into the stack
        zipped = [(position[i],speed[i]) for i in range(len(speed))]
        zipped.sort(reverse=True,key=lambda x:x[0])
        car_fleets = []
        for (p,s) in zipped:
            time_taken = (target - p) / s
            if car_fleets and time_taken > car_fleets[-1]:
                car_fleets.append(time_taken)
            elif not car_fleets:
                car_fleets.append(time_taken)
        return len(car_fleets)
                
