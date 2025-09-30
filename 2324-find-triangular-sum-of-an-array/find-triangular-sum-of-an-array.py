class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newNums = []

        while len(nums) != 1:
            for i in range(len(nums)-1):
                num = (nums[i] + nums[i+1]) % 10
                newNums.append(num)
            nums = newNums
            newNums = []
        return nums[0]
