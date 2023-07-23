class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_vowels = []
        for ch in s:
            if ch in vowels:
                s_vowels.append(ch)

        s_vowels.sort()
        i = 0
        result = ''
        
        for ch in s:
            if ch in vowels:
                result += s_vowels[i]
                i += 1
            else:
                result += ch

        return result
