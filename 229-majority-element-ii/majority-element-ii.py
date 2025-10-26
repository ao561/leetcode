class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = math.floor(len(nums)/3)

        map = defaultdict(int)

        for num in nums:
            map[num] += 1
        
        ans = []

        for key, val in map.items():
            if val > threshold:
                ans.append(key)
        
        return ans


        