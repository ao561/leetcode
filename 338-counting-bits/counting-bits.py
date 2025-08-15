class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            count = 0
            temp_i = i

            while temp_i > 0:
                if temp_i & 1 == 1:
                    count += 1
                temp_i >>= 1
            ans.append(count)
        
        return ans