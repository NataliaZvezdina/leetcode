class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        st = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        cnt_a = cnt_b = 0
        for i, c in enumerate(s):
            if c in st:
                if i < len(s) / 2 : cnt_a +=1
                else: cnt_b += 1

        return cnt_a == cnt_b