class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s)==1:
            return 1
        dict1 = {}
        l,r = 0, 1

        set1 = set(s[l])
        while r<len(s):
            if s[r] != s[l] and s[r] not in set1:
                set1.add(s[r])
                dict1[l] = 1 + dict1.get(l,1)
            else:
                if l not in dict1:
                    dict1[l] = 1
                set1.clear()
                l+=1
                r=l
            r+=1
        max1 = max(dict1.values())

        return max1


        