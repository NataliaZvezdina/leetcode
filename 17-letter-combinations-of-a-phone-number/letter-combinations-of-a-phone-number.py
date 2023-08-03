class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def combo(curr, id):
            if id >= len(digits):
                res.append(curr)
                return

            letters = keys[ord(digits[id])-ord('0')]
            for letter in letters:
                combo(curr+letter, id+1)

        res = []
        if not digits: return res
        
        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combo("", 0)
        return res
