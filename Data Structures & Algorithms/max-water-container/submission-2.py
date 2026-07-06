class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1 = 0

        l,r = 0, len(heights)-1

        while l < r:
            res = min(heights[l],heights[r]) * (r-l)
            max1 = max(res,max1)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            
        return max1