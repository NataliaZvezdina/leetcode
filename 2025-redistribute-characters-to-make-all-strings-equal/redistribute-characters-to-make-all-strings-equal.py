class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp = defaultdict(int)
        for w in words:
            for c in w:
                mp[c] += 1

        for c in mp:
            if mp[c] % len(words):
                return False

        return True
