class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq ={}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for x in freq:
            if freq[x] > 1:
                return True
        return False
