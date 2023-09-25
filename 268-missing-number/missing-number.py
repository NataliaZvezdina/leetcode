class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        for n in range(len(nums)):
            res = res ^ n ^ nums[n]
        return res ^ len(nums)