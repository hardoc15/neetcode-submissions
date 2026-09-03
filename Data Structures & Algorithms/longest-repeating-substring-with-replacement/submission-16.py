class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}

        max1 = 0

        i = 0
        for j in range(len(s)):
            counts[s[j]] = 1 + counts.get(s[j],0)

            if (max(counts.values()) + k) < (j-i+1):
                counts[s[i]] -= 1
                i+=1
            
            max1 = max(max1, j-i+1)
        
        return max1


        