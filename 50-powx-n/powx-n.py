class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        flag = True
        if n < 0:
            n = -n
            flag = False
        while n > 0:
            if n % 2 == 1:
                res *= x
            x = x * x
            n //= 2
        
        return res if flag else 1 / res
