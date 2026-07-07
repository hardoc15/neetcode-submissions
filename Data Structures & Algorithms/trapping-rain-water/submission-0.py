class Solution:
    def trap(self, height: List[int]) -> int:
        max1 = 0

        maxLeft = []
        max1 = 0
        for i in range(len(height)):
            max1 = max(height[i],max1)
            maxLeft.append(max(max1,height[i]))

        maxRight = [0]*len(height)
        max1 = 0
        for i in range(len(height)-1,-1,-1):
            max1 = max(height[i],max1)
            maxRight[i] = (max(max1,height[i]))

        total = 0
        for i in range(len(height)):
            if min(maxRight[i],maxLeft[i]) - height[i] > 0:
                total += min(maxRight[i],maxLeft[i]) - height[i]
            else:
                continue
        return total


            


        