class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            if i % 2:
                if s[i] == '0': cnt += 1
            else:
                if s[i] == '1': cnt += 1

        return min(cnt, len(s)-cnt)
