class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = defaultdict(list)

        for index, num in enumerate(numbers):
            if (target - num) in dict1:
                return sorted([dict1[target-num]+1,index+1])
            dict1[num] = index
        return res
        

        