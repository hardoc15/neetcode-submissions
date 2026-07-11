import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        heap = []
        l=0
        r= 0
        while r < len(nums):
            heapq.heappush(heap,(nums[r]*-1))
            if len(heap) == k:
                res.append((heap[0]*-1))
                heap = []
                l+=1
                r=l
            else:
                r+=1


        return res
        