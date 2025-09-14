class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            if len(stack) == 0 or num >= stack[-1]:
                stack.append(num)
        
        return len(stack)