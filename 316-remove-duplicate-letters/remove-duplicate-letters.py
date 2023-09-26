class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_ocur = {}
        for i,c in enumerate(s):
            last_ocur[c] = i

        stack = []
        visited = set()

        for i in range(len(s)):
            if s[i] in visited: continue
            while stack and stack[-1] > s[i] and last_ocur.get(stack[-1], -1) > i:
                visited.remove(stack.pop())
            visited.add(s[i])
            stack.append(s[i])

        return ''.join(stack)
