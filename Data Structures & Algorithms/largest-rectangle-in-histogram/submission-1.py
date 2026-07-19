class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max1 = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max1 = max(max1, height*(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            max1 = max(max1, h * (len(heights)-i))

        return max1


        