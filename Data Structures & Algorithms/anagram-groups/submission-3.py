class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        list1= []
        for word in strs:
            dict1["".join(sorted(word))].append(word)
        for i in dict1:
            list1.append(dict1[i])
        return list1
