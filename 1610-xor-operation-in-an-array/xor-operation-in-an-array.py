class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n

        for i in range(len(nums)):
            nums[i] = start + 2 * i
        
        x = nums[0]

        for i in range(1, len(nums)):
            x = x ^ nums[i]
        return x
