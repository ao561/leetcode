class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        x = list(s)

        for char in x:
            if char in "AEIOUaeiou":
                vowels.append(char)
        
        if vowels == []:
            return s
        
        vowels.sort()

        count = 0

        for i in range(len(s)):
            if x[i] in "AEIOUaeiou":
                x[i] = vowels[count]
                count += 1

        return "".join(x)