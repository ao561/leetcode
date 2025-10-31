class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        output = ""
        while l < len(word1) and r < len(word2):
            output += (word1[l])
            output += (word2[r])

            l += 1
            r += 1
        
        if l < len(word1):
            output += (word1[l:len(word1)])
        elif r < len(word2):
            output += (word2[r:len(word2)])
        
        return output