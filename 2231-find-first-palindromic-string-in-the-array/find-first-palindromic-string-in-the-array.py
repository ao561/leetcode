class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalindrome(string):
            L, R = 0, len(string) - 1
            while L <= R:
                if string[L] != string[R]:
                    return False
                L += 1
                R -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        
        return ""