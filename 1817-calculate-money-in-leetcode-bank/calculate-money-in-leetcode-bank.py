class Solution:
    def totalMoney(self, n: int) -> int:
        day = 1
        start = 1
        total = 0
        amount = 1

        while n > 0:
            if day % 8 == 0:
                start += 1
                amount = start
                day = 1
              
            total += amount
            amount += 1
            day += 1
            n -= 1
        
        return total