class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: -len(w))
        word_index = {}
        for i,w in enumerate(words):
            word_index[w] = i

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1
            for j in range(len(words[i])):
                w = words[i]
                pred = w[:j] + w[j+1:]
                if pred in word_index:
                    res = max(res, 1 + dfs(word_index[pred]))

            dp[i] = res
            return res

        for i in range(len(words)):
            dfs(i)

        return max(dp.values())
