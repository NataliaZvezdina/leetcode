class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(used, curr=[]):
            if len(curr) == len(nums):
                output.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]): continue
                curr.append(nums[i])
                used[i] = True
                backtrack(used, curr)
                used[i] = False
                curr.pop()

        output = []
        used = [0] * len(nums)
        nums.sort()
        backtrack(used)
        return output
