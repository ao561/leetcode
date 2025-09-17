class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for char in magazine:
            map[char] = map.get(char, 0) + 1

        for char in ransomNote:
            if char not in map:
                return False
            else:
                map[char] -= 1
                if map[char] == 0:
                    map.pop(char)

        
        return True