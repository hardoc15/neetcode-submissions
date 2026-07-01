class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        res = 0

        for i in nums:
            streak = 0
            curr = i
            while curr in set1:
                streak+=1
                curr+=1
            res = max(streak,res)
        return res

    
        