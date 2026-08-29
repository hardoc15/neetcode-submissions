class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            counts[i] = 1 + counts.get(i,0)
        
        res = []

        for val,count in counts.items():
            freq[count].append(val)
        
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        