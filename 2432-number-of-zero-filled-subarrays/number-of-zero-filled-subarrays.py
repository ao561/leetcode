class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cur = 0

        for num in nums:
            if num == 0:
                cur += 1
                ans += cur
            else:
                cur = 0
        return ans