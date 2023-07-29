class Solution:
    def soupServings(self, n: int) -> float:
        m = math.ceil(n/25)
        dp = collections.defaultdict(dict)

        def prob(i, j):
            if i in dp and j in dp[i]:
                return dp[i][j]

            if i <=0 and j > 0:
                return 1
            if i <= 0 and j <= 0:
                return 0.5
            if i > 0 and j <= 0:
                return 0
            
            dp[i][j] = (prob(i-4,j) + prob(i-3,j-1) + prob(i-2,j-2) + prob(i-1,j-3)) / 4.0
            return dp[i][j]

        for k in range(1, m+1):
            if prob(k,k) > 1 - 1e-5:
                return 1.0
        return prob(m,m)
        