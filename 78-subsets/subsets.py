class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                ans.append(sol.copy())
                return
            
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            backtrack(i+1)
        
        backtrack(0)
        return ans