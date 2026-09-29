class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for index, x in enumerate(nums):
            if target - x in found:
                return [index, found[target - x]]
            else:
                found[x] = index
        
        