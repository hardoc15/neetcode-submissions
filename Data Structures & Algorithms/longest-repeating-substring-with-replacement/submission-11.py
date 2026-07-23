class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}

        l,r = 0,0
        i = k
        max1 = 0

        while r < len(s):
            count[s[r]] = 1+ count.get(s[r],0)
            window = r - l+1

            if (window-k) > max(count.values()):
                count[s[l]]-=1
                l+=1
            max1 = max(max1,r-l+1)
            r+=1 
        
        return max1


            
        