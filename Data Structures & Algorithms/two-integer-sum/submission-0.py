class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen.get(target - num), idx]
            seen[num] = idx




