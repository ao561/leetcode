class Solution:
    def trailingZeroes(self, n: int) -> int:
        tz = 0
        i = 1

        while n >= 5**i:
            tz += (n//5**i)
            i += 1
        
        return tz
        



