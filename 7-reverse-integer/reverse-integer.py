class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        res = 0

        if x >= 0:
            res = int(num[::-1])
        elif x < 0:
            res = -1 * int(num[1:][::-1])
        
        if res > (2**31)-1 or res < -2**31:
            return 0
        else:
            return res