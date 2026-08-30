class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums = sorted(nums)

        for index, val in enumerate(nums):
            if val > 0:
                break
            if index > 0 and val == nums[index-1]:
                continue
            
            l,r = index+1, len(nums)-1

            while l < r:
                three = val + nums[l] + nums[r]
                if three > 0:
                    r-=1
                elif three < 0:
                    l+=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        

        return res

        