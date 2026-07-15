class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)

        l,r = 0, 1
        while r <len(temperatures):
            if temperatures[r] > temperatures[l]:
                days[l] = r-l
                l+=1
                r=l
            r+=1
            if r == len(temperatures):
                l+=1
                r=l
        return days
                
                
            

        