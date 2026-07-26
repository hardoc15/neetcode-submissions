class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max1 = 0

        l,r = 0, len(heights)-1

        while l < r:

            w = min(heights[l],heights[r]) * (r-l)

            max1 = max(max1,w)

            if heights[l] < heights[r]:
                w = heights[l] * (r-l)
                l+=1
            else:
                w = heights[r] * (r-l)
                r-=1
            
        return max1