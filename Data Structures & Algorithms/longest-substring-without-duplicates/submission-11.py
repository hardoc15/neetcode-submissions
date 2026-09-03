class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set1 = set()

        max1 = 0
        i =0
        for j in range(len(s)):
            while s[j] in set1:
                set1.remove(s[i])
                i+=1
            set1.add(s[j])
            max1 = max(max1,j-i+1)
        
        return max1

