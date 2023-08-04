class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = deque([0])
        used = set()
        
        while q:
            start = q.popleft()
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                if end in used:
                    continue
                
                if s[start:end] in words:
                    q.append(end)
                    used.add(end)
                
        return False
