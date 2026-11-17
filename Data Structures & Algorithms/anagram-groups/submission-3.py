class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if I can rearrange the letters of two words to look the same they are anagrams
        d = defaultdict(list)
        print(d)
        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS].append(s)
        return list(d.values())