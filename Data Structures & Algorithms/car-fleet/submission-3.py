import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed),reverse=True)

        times = []
        slowest = 0.0
        for position,speed in cars:
            time = (target-position) / speed

            if time > slowest:
                times.append(time)
                slowest =time
        
        return len(times)

        

        
        