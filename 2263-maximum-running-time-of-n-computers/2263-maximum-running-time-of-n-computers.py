class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l = 1
        r = 10 ** 14
        ans = 1
        
        def ok(time):
            power = 0
            for i in range(len(batteries)):
                if batteries[i] >= time:
                    power += time
                else:
                    power += batteries[i]

            return power / n >= time


        while l <= r:
            mid = (l+r) // 2
            if ok(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans