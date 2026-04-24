class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for string in strs:
            if "".join(sorted(string)) not in seen:
                seen["".join(sorted(string))] = [string]
            else:
                seen["".join(sorted(string))].append(string)

        return list(seen.values())
        


