class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        x = []
        for i in range(len(nums)):
            if nums[i] in hashMap:
                x.append(nums[i])
            else:
                hashMap[nums[i]] = 1
        return x