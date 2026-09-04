class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dict1 = {}
        max1 = 0
        i=0
        for j in range(len(s)):
            dict1[s[j]] = 1 + dict1.get(s[j],0)
            if (max(dict1.values()) + k) < (j-i+1):
                dict1[s[i]]-=1
                i+=1
            max1 = max(max1, (j-i+1))
        
        return max1
        