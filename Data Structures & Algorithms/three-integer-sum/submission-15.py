class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums = sorted(nums)

        for index, val in enumerate(nums):
            
            if val > 0:
                break
            
            if index > 0 and val == nums[index-1]:
                continue

            i,j = index+1, len(nums)-1
            while i < j:
                num = val + nums[i] + nums[j]
                if num > 0:
                    j -= 1
                elif num <0:
                    i+=1
                else:
                    res.append([val,nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i-1]:
                        i+=1
                    
                
        return res
        