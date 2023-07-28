class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}

        def max_diff(left, right):
            if (left, right) in dp:
                return dp[(left, right)]
            if left == right:
                return nums[left]

            dp[(left, right)] = max(nums[left] - max_diff(left + 1, right), nums[right] - max_diff(left, right - 1))
            return dp[(left, right)]

        return max_diff(0, len(nums)-1) >= 0
