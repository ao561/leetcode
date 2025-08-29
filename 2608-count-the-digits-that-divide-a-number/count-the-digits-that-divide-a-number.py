class Solution:
    def countDigits(self, num: int) -> int:
        string = str(num)
        count = 0
        map = {}

        for char in string:
            if num % int(char) == 0 and char not in map:
                count += 1
            else:
                map[char] = map.get(char, 0) + 1
        
        return count 