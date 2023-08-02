class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr=[]):
            if len(curr) == len(nums):
                output.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()

        output = []
        backtrack()
        return output
        