class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 0:
            return 0

        arr1 = nums[:(n-1)]
        arr2 = nums[1:]

        def dp(nums):
            n = len(nums)

            if n < 3:
                return max(nums)
                
            prev, cur = nums[0], max(nums[0], nums[1])

            for i in range(2, n):
                prev, cur = cur, max(cur, prev + nums[i])
            
            return cur
        
        return max(dp(arr1), dp(arr2))