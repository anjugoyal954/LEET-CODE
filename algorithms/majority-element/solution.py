class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for x in freq:
            if freq[x] > n/2:
                return x