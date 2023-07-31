class Solution:
    def climbStairs(self, n: int) -> int:

        def count(st, memo):
            if st <= 2:
                return st
            if memo[st] != -1:
                return memo[st]

            memo[st] = count(st-1, memo) + count(st-2, memo)
            return memo[st]


        memo = [-1] * (n+1)
        return count(n, memo)
        