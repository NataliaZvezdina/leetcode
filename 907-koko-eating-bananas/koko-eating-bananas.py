class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = 10 ** 9

        ans = 10 ** 9

        def ok(k):
            tm = 0
            for pile in piles:
                tm += ceil(pile / k)

            return tm <= h


        while l <= r:
            mid = (l+r) // 2
            if ok(mid):
                r = mid - 1
                ans = mid
            else: 
                l = mid + 1

        return ans