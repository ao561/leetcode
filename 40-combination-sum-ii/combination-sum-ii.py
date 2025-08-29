class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, res = [], []
        nums = candidates
        n = len(nums)
        nums.sort()

        def backtrack(i, curSum):
            if curSum == target:
                ans.append(res.copy())
                return
            if i == n or curSum > target:
                return
            
            res.append(nums[i])
            backtrack(i + 1, curSum + nums[i])
            res.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, curSum)
        
        backtrack(0,0)
        return ans


