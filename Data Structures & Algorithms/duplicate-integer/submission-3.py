class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # Get possible duplicates next to each other
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1: # prevent index out of range
                return False
            if nums[idx] == nums[idx + 1]: # if siblings eq, True
                return True
        return False