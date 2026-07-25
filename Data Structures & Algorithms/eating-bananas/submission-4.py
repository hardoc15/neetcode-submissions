import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max1 = max(piles)

        res = max1

        r = max1
        l = 1

        while l <= r:
            w = (l+r) // 2
            count = 0
            for p in piles:

                count+= math.ceil(p/w)
            
            if count <= h:
                res = min(res,w)
                r= w-1
            else:
                l=w+1
            
        return res