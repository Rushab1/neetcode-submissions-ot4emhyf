class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for s in strs:
            k = str(sorted(s))
            l[k].append(s)

        return list(l.values())
