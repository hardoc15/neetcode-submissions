class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for word in strs:
            dict1["".join(sorted(word))].append(word)
        return list(dict1.values())
