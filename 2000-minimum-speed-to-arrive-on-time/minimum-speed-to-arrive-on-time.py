class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = 10 ** 7
        ans = -1

        def ok(sp):
            t = 0
            for i in range(len(dist)-1):                
                t += math.ceil(dist[i] / sp)
            t += dist[-1] / sp
            return t <= hour


        while l <= r:
            mid = (l+r) // 2
            if ok(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        
        return ans