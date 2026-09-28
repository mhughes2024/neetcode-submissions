class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} # value -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store: # check if complement already exists
                return [store[diff], i] # return index of   complement, current index
            store[num] = i # store value -> index in map
            
            
            
        