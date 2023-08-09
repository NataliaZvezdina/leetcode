class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        l = 0
        r = ans = abs(nums[0]-nums[-1])

        def ok(diff):
            cnt = 0
            idx = 0
            while idx < len(nums)-1:
                if nums[idx+1]-nums[idx] <= diff:
                    cnt += 1
                    idx += 1
                idx += 1
            return cnt >= p


        while l <= r:
            mid = (l+r) // 2
            if ok(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1

        return ans
