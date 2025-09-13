class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelmap = {}
        consmap = {}
        maxcons = 0
        maxvowel = 0

        for char in s:
            if char in "aeiou":
                vowelmap[char] = vowelmap.get(char, 0) + 1
            else:
                consmap[char] = consmap.get(char, 0) + 1

        for key, val in vowelmap.items():
            if val >= maxvowel:
                maxvowel = val

        for key, val in consmap.items():
            key = 0
            if val >= maxcons:
                maxcons = val
        
        return maxcons + maxvowel

