class Solution:
    def strangePrinter(self, s: str) -> int:

        def solve(i, j, dp):
            if i == j:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            min_turns = math.inf
            for k in range(i,j):
                min_turns = min(min_turns, solve(i, k, dp) + solve(k+1, j, dp))

            dp[i][j] = min_turns - 1 if s[i] == s[j] else min_turns
            return dp[i][j]

        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return solve(0, len(s)-1, dp)