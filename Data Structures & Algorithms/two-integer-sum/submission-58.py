class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, val in enumerate(nums):
            if (target - val) in seen:
                return sorted((index,seen[target-val]))
            seen[val] = index
        
        return -1