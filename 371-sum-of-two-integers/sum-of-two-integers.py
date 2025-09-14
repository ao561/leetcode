class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask & b) > 0:
            tmp = (a & b) << 1  
            a = a ^ b
            b = tmp
        return (mask & a) if b > 0 else a

        