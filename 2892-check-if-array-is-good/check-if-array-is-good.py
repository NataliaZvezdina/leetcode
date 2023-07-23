from collections import defaultdict

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1

        if len(mp) != len(nums) - 1:
            return False

        for i in range(1, len(nums)-1):
            if mp[i] != 1:
                return False

        if mp[len(nums)-1] != 2:
            return False
        
        return True