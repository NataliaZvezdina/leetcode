class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def compute(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i < 0 and j < 0:
                return 0

            if i < 0:
                memo[(i,j)] = ord(s2[j]) + compute(i, j-1)
                return memo[(i,j)]
            if j < 0:
                memo[(i,j)] = ord(s1[i]) + compute(i-1, j)
                return memo[(i,j)]

            if s1[i] == s2[j]:
                memo[(i,j)] = compute(i-1, j-1)
            else:
                memo[(i,j)] = min(ord(s1[i]) + compute(i-1, j), ord(s2[j]) + compute(i, j-1))

            return memo[(i,j)]

        return compute(len(s1)-1, len(s2)-1)

            