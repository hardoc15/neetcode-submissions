class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        max1 = 0
        for i in nums:
            count = 1
            if (i-1) not in seen:
                while (i+count) in seen:
                    count+=1
                max1 = max(max1, count)
        return max1
