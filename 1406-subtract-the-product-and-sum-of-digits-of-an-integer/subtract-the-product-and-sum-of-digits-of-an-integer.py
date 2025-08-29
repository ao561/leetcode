class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        prod = 1

        for char in str(n):
            add += int(char)
            prod *= int(char)
        
        return prod - add