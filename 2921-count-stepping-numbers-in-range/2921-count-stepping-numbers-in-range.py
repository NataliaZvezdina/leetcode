class Solution:
    def countSteppingNumbers(self, num1: str, num2: str) -> int:
        

        def countStrings(i, tight, leading, num, prev=-1):
            if i == len(num):
                return 1
            if dp[i][tight][leading][prev+1] != -1:
                return dp[i][tight][leading][prev+1]

            hi = 9 if tight == 0 else ord(num[i]) - ord('0')
            cnt = 0
            for idx in range(hi+1):
                if prev != -1 and not leading:
                    if abs(prev-idx) == 1:
                        cnt = (cnt % MOD + (countStrings(i+1, tight&(idx==hi), leading&(idx==0), num, idx) % MOD)) % MOD
                    continue
                
                cnt = (cnt % MOD + (countStrings(i+1, tight&(idx==hi), leading&(idx==0), num, idx) % MOD)) % MOD

            dp[i][tight][leading][prev+1] = cnt
            return dp[i][tight][leading][prev+1]


        dp = [[[[-1 for _ in range(11)] for _ in range(2)] for _ in range(2)] for _ in range(101)]
        MOD = 10 ** 9 + 7
        a = countStrings(0, 1, 1, num1)
        valid = 1
        for i in range(1,len(num1)):
            if abs(ord(num1[i])-ord(num1[i-1])) != 1:
                valid = 0
                break
        a -= valid


        dp = [[[[-1 for _ in range(11)] for _ in range(2)] for _ in range(2)] for _ in range(101)]
        b = countStrings(0, 1, 1, num2)
        return (b - a + MOD) % MOD
