class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set1 = set(nums)
        res = 0
        for i in nums:
            count = 0
            curr = i
            while curr in set1:
                count+=1
                curr+=1
            res = max(res,count)
        return res


        