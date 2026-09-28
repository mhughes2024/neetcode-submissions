class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # sorted str -> list unsorted strs
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # store freq of c
            res[tuple(count)].append(s)
        return list(res.values())