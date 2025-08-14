class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        for key, val in map.items():
            if val == 1:
                return key