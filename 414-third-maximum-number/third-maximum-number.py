class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        if len(num) >= 3:
            return num[-3]
        else:
            return max(nums)