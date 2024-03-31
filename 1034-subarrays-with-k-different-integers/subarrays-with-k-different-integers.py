class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res = 0
        l_far, l_near = 0, 0
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            while len(cnt) > k:
                cnt[nums[l_near]] -= 1
                if cnt[nums[l_near]] == 0:
                    cnt.pop(nums[l_near])
                l_near += 1
                l_far = l_near
            while cnt[nums[l_near]] > 1:
                cnt[nums[l_near]] -= 1
                l_near += 1

            if len(cnt) == k:
                res += l_near - l_far + 1

        return res
