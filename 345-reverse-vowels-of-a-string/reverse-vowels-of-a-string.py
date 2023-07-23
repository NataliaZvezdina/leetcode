class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_vowels = []
        for ch in s:
            if ch in vowels:
                s_vowels.append(ch)

        i = len(s_vowels) - 1
        result = ''
        
        for ch in s:
            if ch in vowels:
                result += s_vowels[i]
                i -= 1
            else:
                result += ch

        return result