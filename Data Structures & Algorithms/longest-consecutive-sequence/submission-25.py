class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        max1 = 0
        for i in nums:
            if (i-1) in nums:
                continue
            count = 1
            while (i+count) in nums:
                count+=1
            max1 = max(max1,count)
        
        return max1