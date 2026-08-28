class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        counts = {}
        max1 = 0
        for i in nums:
                counts[i] = 1 + counts.get((i-1),0)
                max1 = max(max1,counts[i])
 
        
        return max1

