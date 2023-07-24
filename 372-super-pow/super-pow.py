class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n = int(''.join([str(digit) for digit in b]))
        MOD = 1337

        res = 1
        while n > 0:
            if n % 2 == 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            n //= 2
        return res