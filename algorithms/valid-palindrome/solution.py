class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        output = 0
        for i in nums:
            output = output ^ i #XOR -- ^
        return output
            
        
