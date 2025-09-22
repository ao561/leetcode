class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        max_freq = 0

        for key, val in map.items():
            if val > max_freq:
                max_freq = val

        total = 0

        for key, val in map.items():
            if val == max_freq:
                total += val

        return total
        
