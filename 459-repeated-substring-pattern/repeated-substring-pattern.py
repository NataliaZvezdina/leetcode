class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        factors = []
        i = 2
        n = len(s)
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if n // i != i:
                    factors.append(n // i)
            i += 1
        
        factors.sort(reverse=True)
        factors.append(1)
       
        for ln in factors:
            sample = s[:ln] + '#' + s
            p_sample = [0] * len(sample)
            for i in range(1, len(sample)):
                j = p_sample[i - 1]
                while j > 0 and sample[j] != sample[i]:
                    j = p_sample[j - 1]
                if sample[i] == sample[j]:
                    j += 1
                p_sample[i] = j

           
            i = 2 * ln
            while i < len(sample) and p_sample[i] == ln:
                i += ln
            if i >= len(sample):
                return True

        return False
