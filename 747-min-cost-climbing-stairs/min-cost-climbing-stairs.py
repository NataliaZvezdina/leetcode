class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def cnt(i, memo):
            if i <= 1:
                return cost[i]

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(cnt(i-1,memo), cnt(i-2,memo))
            return memo[i]

        memo = {}
        cost.append(0)
        return cnt(len(cost)-1, memo)
        