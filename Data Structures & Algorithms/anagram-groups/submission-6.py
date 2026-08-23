class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs:
            x = tuple(sorted(i))
            seen[x].append(i)
        
        return list(seen.values())
            
