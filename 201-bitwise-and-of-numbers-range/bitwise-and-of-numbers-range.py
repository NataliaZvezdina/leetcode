class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0

        for i in range(32):
            bit = (left >> i) & 1
            if not bit:
                continue


            remainder = left % (1 << (i + 1))
            diff = (1 << (i + 1)) - remainder

            if right - left < diff:
                res  = res | (1 << i)
                
        return res