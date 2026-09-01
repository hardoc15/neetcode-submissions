class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set1 = set()

        i=0
        res = 0

        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[i])
                i+=1
            set1.add(s[r])
            res = max(res,r-i+1)
        
        return res

        