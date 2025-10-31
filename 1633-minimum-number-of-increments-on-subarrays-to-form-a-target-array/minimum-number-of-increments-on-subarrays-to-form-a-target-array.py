class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev, total = 0, 0
        for x in target:
            if x > prev:
                total += x - prev
            prev = x
        
        return total