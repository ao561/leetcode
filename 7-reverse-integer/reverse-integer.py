class Solution:
    def reverse(self, x: int) -> int:
        min_int, max_int = -2**31, 2**31-1
        reversed_x = 0
        
        sign = -1 if x < 0 else 1

        x = abs(x)

        while x:
            digit = x%10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        reversed_x *= sign
        if reversed_x < min_int or reversed_x > max_int:
            return 0
        return reversed_x