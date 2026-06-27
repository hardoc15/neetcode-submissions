class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for key,value in dict1.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        

        


        