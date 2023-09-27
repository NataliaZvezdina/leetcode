class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decod_len = [0] * len(s)
        decod_len[0] = 1
        i = 1
        while decod_len[i-1] < k:
            if not s[i].isnumeric():
                decod_len[i] = decod_len[i-1] + 1
            else:
                decod_len[i] = int(s[i]) * decod_len[i-1]
            i += 1

        i -= 1
        while decod_len[i] > k:
            i -= 1
            if decod_len[i] < k:
                k = (k-1) % decod_len[i] + 1

        while s[i].isnumeric(): i -= 1
        return s[i]
        