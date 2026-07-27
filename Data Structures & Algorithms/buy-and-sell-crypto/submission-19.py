class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r = 0, 1
        max1=0

        while l <= r and r < len(prices):
            if prices[l] < prices[r]:
                max1 = max((prices[r]-prices[l]),max1)

            elif prices[r] < prices[l]:
                l+=1
                continue
            
            r+=1
        
        return max1

