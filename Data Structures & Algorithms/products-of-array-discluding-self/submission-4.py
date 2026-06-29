class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        list1 = []
        zeros = 0
        
        for i in range(0,len(nums)):
            if nums[i] != 0:
                total*= nums[i]
            else:
                zeros+=1
            
        if zeros >= 2:
            return [0] * len(nums)

        elif zeros > 0:
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    list1.append(total)
                else:
                    list1.append(0)
        else:
            for i in range(0,len(nums)):
                list1.append(int(total/nums[i]))

        return list1
        
            
            

            

        

