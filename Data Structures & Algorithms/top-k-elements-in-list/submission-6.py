class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        
        for n,c in dict1.items():
            freq[c].append(n) 
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return res


        

        


        