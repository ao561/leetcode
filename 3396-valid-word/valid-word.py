class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiou"
        vowels += vowels.upper()
        consonants = "qwrtypsdfghjklzxcvbnm"
        consonants += consonants.upper()
        allowed = vowels + consonants + "0123456789"
        
        if len(word) < 3:
            return False

        hasVowel = False
        hasCons = False

        for char in word:
            if char in vowels:
                hasVowel = True
            if char in consonants:
                hasCons = True
            if char not in allowed:
                return False
            
        return hasVowel and hasCons
            