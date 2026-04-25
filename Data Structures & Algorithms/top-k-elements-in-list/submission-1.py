class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        seen = sorted(seen, key=lambda x: seen[x], reverse=True)
        return seen[:k]







        