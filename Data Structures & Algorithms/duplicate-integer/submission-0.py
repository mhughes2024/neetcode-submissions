class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = []
        for num in nums:
            if num not in container:
                container.append(num)
            else:
                return True

        return False
         