class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        
        for char in s:
            if hashMap[char] == 1:
                return s.index(char)
        return -1