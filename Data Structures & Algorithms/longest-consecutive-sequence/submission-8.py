class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        counts = {}

        for i in nums:
                counts[i] = 1 + counts.get((i-1),0)
        
        return max(counts.values())

