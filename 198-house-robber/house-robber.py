class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) < 3:
            return max(nums)
            
        prev, cur = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            prev, cur = cur, max(cur, prev + nums[i])
        
        return cur

