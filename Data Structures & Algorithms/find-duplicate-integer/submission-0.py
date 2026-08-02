class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dict1 = {}

        for i in nums:
            if i in dict1:
                return i
            else:
                dict1[i] = 1
        
        

        