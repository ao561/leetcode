class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        count = 0

        for char in x:
            if char == "1":
                count += 1
        
        return count 